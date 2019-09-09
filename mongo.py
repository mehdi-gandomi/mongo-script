#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient
client = MongoClient()
#client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017')


# In[2]:


db = client.test
#db = client['pymongo_test']


# In[3]:


users = db.users
user_data = {
    'username': 'Coderguy',
    'name': 'Mehddi',
    'pass': '123'
}
result = users.insert_one(user_data)
print('One post: {0}'.format(result.inserted_id))


# In[5]:


user1 = {
    'username': 'Coderguy2',
    'name': 'Mehddi2',
    'pass': '1234'
}
user2 = {
    'username': 'Coderguy3',
    'name': 'Mehddi3',
    'pass': '12345'
}
result=users.insert_many([user1,user2])
print('One post: {0}'.format(result.inserted_ids))


# In[6]:


user = users.find_one({'username': 'Coderguy'})
print(user)


# In[9]:


allusers = users.find({'username': 'Coderguy2'})
print(allusers)
for user in allusers:
    print(user)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




