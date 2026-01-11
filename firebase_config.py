import pyrebase

firebaseConfig = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_PROJECT.firebaseapp.com",
    "projectId": "YOUR_PROJECT",
    "storageBucket": "YOUR_PROJECT.appspot.com",
    "messagingSenderId": "",
    "appId": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
