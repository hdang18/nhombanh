import os
import json
import uuid

posts_dir = 'content/posts'
output_file_path = 'content/posts.json'

if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)
    print(f"Directory {posts_dir} created.")

if os.path.exists(output_file_path):
    with open(output_file_path, 'r') as f:
        data = json.load(f)
        existing_posts = data.get('posts', [])
else:
    existing_posts = []

posts_from_dir = []
for filename in os.listdir(posts_dir):
    if filename.endswith('.json'):
        with open(os.path.join(posts_dir, filename)) as f:
            post = json.load(f)
            if 'id' not in post:
                post['id'] = str(uuid.uuid4())
            posts_from_dir.append(post)

existing_titles = {post['title'] for post in existing_posts}

post_titles_from_dir = {post['title'] for post in posts_from_dir}
updated_posts = [post for post in existing_posts if post['title'] in post_titles_from_dir]
updated_posts.extend(post for post in posts_from_dir if post['title'] not in existing_titles)

with open(output_file_path, 'w') as f:
    json.dump({"posts": updated_posts}, f, indent=2)

print("posts.json has been updated!")
