import os

programa="brave-browser"
args=("google.com",)
# args={"google.com"}


print("iniciando o processo pai")

input("digite ENTER")
os.execvp(programa,(programa,)+tuple(args))

print("finalizando processo....")