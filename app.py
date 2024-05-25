import streamlit as st
import requests
import json

host = "https://lists-api.onrender.com"
username = "SJ"
my_items_url = f"/{username}/items"
send_item_url = f"/items/send"

def get_items():
    res = requests.get(host + my_items_url)
    if res.status_code == 200:
        return json.loads(res.json()['results'])
    return []

def send_item(user, content):
    body = {
        "user": user,
        "content": content,
        "added_by": "MJ"
    }
    res = requests.post(host + send_item_url, json=body)
    if res.status_code == 200:
        st.info("Item sent!")
    else:
        st.error("Failed to send item!")

st.title('Hello, SJ')

content = st.text_area('Enter a link')
user = st.selectbox('Select a user', ["SJ", "MJ", "VG"])

if st.button('Send'):
    send_item(user, content)
    
st.header("Here are your items")
items = get_items()
for item in items:
    st.info(item['content'])
    