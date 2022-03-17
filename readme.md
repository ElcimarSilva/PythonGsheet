# Video explicativo
https://www.youtube.com/watch?v=ZU30e4gkV8g


# Instruções execução do projeto
Criar ambiente virtual
instalar biblioteca
configurar e executar projeto

# Biblioteca necessaria
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Links uteis
https://developers.google.com/sheets/api/quickstart/python
https://console.cloud.google.com/apis/credentials?hl=pt-br&project=integracaogsheet-333922
https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append?apix_params=%7B%22spreadsheetId%22%3A%22%5B%5C%22100%5C%22%2C%20%5C%222200%5C%22%5D%22%2C%22range%22%3A%22A%3AB%22%2C%22includeValuesInResponse%22%3Atrue%2C%22insertDataOption%22%3A%22OVERWRITE%22%2C%22responseDateTimeRenderOption%22%3A%22FORMATTED_STRING%22%2C%22responseValueRenderOption%22%3A%22FORMATTED_VALUE%22%2C%22valueInputOption%22%3A%22USER_ENTERED%22%2C%22resource%22%3A%7B%22range%22%3A%22%22%7D%7D


# Instruções basicas do projeto
1-Passo criar projeto no google cloud
2-Passo criar app na Tela de permissão OAuth
3-Passo criar credencial OAuth

1-Passo Pegar código exemplo na documentação
2-Alterar ID da planilha
3-Alterar Range da planilha
4-Baixar credenciais do google cloud e colocar no codigo.
5-Retirar escopo read only para poder editar