from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '10QWyaTRxVWMz5oOxzA2dkfooHHh0MHV9G3Cf_xfipXU' # id da planilha
SAMPLE_RANGE_NAME = 'Página1!A:B' # intervalo de celulas da planilha


def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    # Ler a planilha
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    # else:
    #     for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            #print('%s, %s' % (row[0], row[4]))
    print(values)

    #adicionar ou atualizar
    valores_adicionar = [
        ["Cima", "001"],
        ["Nat", "002"],
    ]
    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range='Página1!A2', valueInputOption='USER_ENTERED',
                                   body={'values': valores_adicionar}).execute()

if __name__ == '__main__':
    main()