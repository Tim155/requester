import requests
from tkinter import *

from requests.api import head

root = Tk()

root.title("Requester")
root.geometry("800x800")

urlLbl = Label(root, text="URL")
urlLbl.pack(pady=(20, 0))

urlInput = Entry(root, textvariable="URL")
urlInput.pack(pady=(0, 20), ipady=10, ipadx=280)

options = ["GET", "POST", "PUT", "DELETE"]
methodInput = StringVar(root)
methodInput.set(options[0])

method = OptionMenu(root, methodInput, *options)
method.pack(ipadx=15)

headerLbl = Label(root, text="Header")
headerLbl.pack(pady=(20, 0))

headerInput = Entry(root)
headerInput.pack(ipady=10, ipadx=280)

dataLbl = Label(root, text="Data")
dataLbl.pack(pady=(20, 0))

dataInput = Entry(root)
dataInput.pack(ipady=10, ipadx=280)

jsonLbl = Label(root, text="JSON")
jsonLbl.pack(pady=(20, 0))

jsonInput = Entry(root)
jsonInput.pack(ipadx=280, ipady=10)

outputTextField = Text(root, state=DISABLED)

count = 1


def insertText(text, field=outputTextField):
    field["state"] = NORMAL
    field.insert(END, text)
    field["state"] = DISABLED


def send():
    global count
    counterText = f"\n{count} --------------------------------\n"
    try:
        url = urlInput.get()
        header = headerInput.get()
        data = dataInput.get()
        json = jsonInput.get()
        try:
            if header != "":
                header = eval(header)
            else:
                header = None
            if data != "":
                data = eval(data)
            else:
                data = None
            if json != "":
                json = eval(json)
            else:
                json = None
        except Exception:
            print("Can't convert...")

        request = None
        arguments = None

        if url != "":
            arguments = [url, header, data, json]

        if methodInput.get() == "GET" and arguments:
            request = requests.get(
                url=arguments[0],
                headers=arguments[1],
                data=arguments[2],
                json=arguments[-1],
            )
            # print("GET:\n", request)

        elif methodInput.get() == "POST" and arguments:
            request = requests.post(
                url=arguments[0],
                headers=arguments[1],
                data=arguments[2],
                json=arguments[-1],
            )
            # print("POST:\n", request)

        elif methodInput.get() == "PUT" and arguments:
            request = requests.put(
                url=arguments[0],
                headers=arguments[1],
                data=arguments[2],
                json=arguments[-1],
            )
            # print("PUT:\n", request)

        elif methodInput.get() == "DELETE" and arguments:
            request = requests.delete(
                url=arguments[0],
                headers=arguments[1],
                data=arguments[2],
                json=arguments[-1],
            )
            # print("DELETE:\n", request)

        if request:
            textInsert = f"{methodInput.get()}: {request.status_code}\n {request.text}"
            insertText((counterText, textInsert))
            count += 1
        else:
            insertText((counterText, request.status_code))
            count += 1

    except Exception:
        insertText((counterText, request.status_code))
        count += 1


def clear():
    global count
    count = 1
    outputTextField["state"] = NORMAL
    outputTextField.delete("1.0", END)
    outputTextField["state"] = DISABLED


submit = Button(root, text="Send", command=send)
submit.pack(pady=(30, 0), ipadx=15)

clearBtn = Button(root, text="Clear", command=clear)
clearBtn.pack(ipadx=15, pady=(10, 10))

closeBtn = Button(root, text="Quit", command=quit)
closeBtn.pack(pady=10, ipadx=10)


outputTextField.pack(pady=10, ipadx=20)


root.mainloop()
