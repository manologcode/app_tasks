from app.models import db, Tag

def get_all_tags():
    return Tag.query.all()

def get_tag_by_id(tag_id):
    return Tag.query.get(tag_id)

def create_tag(request):
    new_tag = Tag(
        name=request.form.get('name'),
        active=request.form.get('active', True)
    )
    db.session.add(new_tag)
    db.session.commit()
    return new_tag

def update_tag(tag_id, data):
    tag = Tag.query.get(tag_id)
    if tag:
        tag.name = data.get('name', tag.name)
        return tag
    return None

def delete_tag(tag_id):
    tag = Tag.query.get(tag_id)
    if tag:
        db.session.delete(tag)
        db.session.commit()
        return True
    return False
