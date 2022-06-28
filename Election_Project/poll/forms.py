from django.forms import ModelForm
from .models import Poll
class CreatePollForm(ModelForm):
    class Meta:
        model=Poll 
        fields=['question','candidate_one','candidate_two','candidate_three']
     