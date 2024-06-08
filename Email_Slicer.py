# AN Email SLicer is very useful program for seperating the username & domain name of an email address.

#chandresh.rajpoot2021@vitstudent.ac.in(example)

email = input("Please enter your email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your username is: '{username}' and your domain name is: '{domain_name}'")
print(format_)
