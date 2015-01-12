'''
A simple python script to create wordpress pages using wordpress_xmlrpc
'''
from wordpress_xmlrpc import Client, WordPressPost, WordPressPage
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

def connect():
    """
    connects to wordpress site. replace "username" and "password" with your actual username and password
    """
    wp = Client('http://madhuram.org/xmlrpc.php', 'USERNAME', 'PASSWORD')
    return wp

def get_pages(wp):
    return wp.call(GetPosts({'post_type': 'page', 'orderby': 'title', 'order': 'ASC', 'number': 130}, results_class=WordPressPage))

def create_post(wp, d):
    post = WordPressPost()
    post.title = d['title']
    post.content = d['content']
    wp.call(NewPost(post))

def create_page(wp, d):
    page = WordPressPage()
    page.title = d['title']
    page.content = d['content']
    page.post_status = 'private'
    wp.call(NewPost(page))

def main():
    """
    Connects to wordpress and creates pages with a simple template.
    """
    wp = connect()
    f = open('authors.text').readlines()
    f.sort()
    for a in f:
       a = a.strip()
       content = '<h1>%s</h1><div style="float:left;width:40%%;"><a href="https://madhuramdotorg.files.wordpress.com/2014/12/%s1.jpg"><img class="alignnone size-medium wp-image-306" src="https://madhuramdotorg.files.wordpress.com/2014/12/%s1.jpg?w=300" alt="%s" width="300" height="199" /></a></div><div style="float:right;width:40%%;"><strong>Email: </strong><strong>Website: </strong></div><div><div><h2>Bio</h2></div></div>' % (a, a.lower(), a.lower(),a)
       d = { 'title' : a, 'content' :content}
       create_page(wp, d)

if __name__ == '__main__':
   main()
