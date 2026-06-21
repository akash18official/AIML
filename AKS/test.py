from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


credential = DefaultAzureCredential()


client = SecretClient(
    vault_url="https://prj-key-vault.vault.azure.net/",
    credential=credential
)

secret = client.get_secret("open-ai-api-key")
print(secret)