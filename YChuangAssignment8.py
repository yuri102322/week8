#!/usr/bin/env python
# coding: utf-8

# In[11]:


class University:
    
    def __init__(self, university_name: str,
                location: str, undergraduate_students: int, graduate_students: int):
        self.university_name = university_name
        self.location = location
        self.undergraduate_students = undergraduate_students
        self.graduate_students = graduate_students
        
    def print_university_size(self):
        print(self.undergraduate_students + self.graduate_students)
        
    def is_undergraduate_greater(self):
        if self.undergraduate_students > self.graduate_students:
            print(f"There are more undergraduate students than graduate students")
        else:
            print(f"There are more graduate students than undergraduate students")


# In[12]:


SPU = University(university_name = "SPU", location = "Jersey City", 
                 undergraduate_students = 2131, graduate_students = 811)


# In[13]:


SPU.print_university_size()


# In[14]:


SPU.is_undergraduate_greater()


# In[22]:


class College(University):
    
    def print_university_colleges(self):
        print(f"{self.university_name} is in {self.location} with {self.undergraduate_students} undergrads and {self.graduate_students} graduates")


# In[23]:


MONROE = College(university_name = "MONROE", location = "Bronx",
                undergraduate_students = 6445, graduate_students = 6541)


# In[24]:


MONROE.print_university_colleges()


# In[25]:


MONROE.print_university_size()


# In[26]:


MONROE.is_undergraduate_greater()


# In[ ]:




