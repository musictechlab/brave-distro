from django.db import models
from django.conf import settings


class Release(models.Model):
    album = models.ForeignKey('albums.Album', on_delete=models.CASCADE, related_name='releases', help_text="Related album.")
    partner = models.ForeignKey('partners.Partner', on_delete=models.CASCADE, related_name='releases', help_text="Related partner.")
    is_dolby_atmos = models.BooleanField(default=False, help_text="Indicates if the release is in Dolby Atmos format.")
    date_original_release = models.DateField(help_text="Original release date.")

    def __str__(self):
        return self.product_title
    

class ReleaseHistory(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='history', help_text="Related release.")
    change_date = models.DateTimeField(auto_now_add=True, help_text="The date and time of the change.")
    changed_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, help_text="The user who made the change.")
    change_description = models.TextField(help_text="Description of the change.")

    def __str__(self):
        return f"{self.release} - {self.change_date}"
    

class ReleasePlatform(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='releases', help_text="Related release.")
    platform = models.ForeignKey('platforms.Platform', on_delete=models.CASCADE, related_name='releases', help_text="Related release.")
   
    def __str__(self):
        return f"{self.release} - {self.platform}"
    

class ReleaseReview(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='releases_reviews', help_text="Related release.")
    date_updated = models.DateField(auto_now=True, help_text="The date when the review was last updated.")
    date_added = models.DateField(auto_now_add=True, help_text="The date when the review was added.")
    release_date = models.DateField(help_text="The release date of the reviewed item.")

    def __str__(self):
        return f"Review for release on {self.release_date} - Status: {self.status}"
   

    def __str__(self):
        return f"{self.release} - {self.release_date}"