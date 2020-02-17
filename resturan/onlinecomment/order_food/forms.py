from django import forms
from django.utils.translation import ugettext_lazy as _


from .models import Comment


class UserCommentForm(forms.Form):
    error_message=_(
        'cannot be empty only contain spaces .please fill the blank field'

    )
    comment=forms.CharField() 

    class Meta:

        model=Comment  
        fields=['comment']

    def clean_comment(self):

        comment=self.cleaned_data.get('comment')
        if comment:

            if not comment.strip():

                raise forms.ValidationError(self.error_message)
        return comment 
class CommentForm(UserCommentForm):

    Author=forms.CharField(lable=_('Author'),initial=_('anonymous')) 
    Date=forms.CharField(lable=_('Date'),required=False)   

    class Meta:
        model=Comment
        fields=('Author','comment','Date') 

    def clean_user_name(self):
        self.error_message
        Author=self.cleaned_data.get('Author') 

        if Author:
            if not Author.strip():

                raise forms.ValidationError(self.error_message)  
        return Author                 
