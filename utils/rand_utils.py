from usercategory.models import *

class RandUtils:

    @staticmethod
    def upadate_or_create_user_category(user, benef_categiory):
        UserCategory.objects.get_or_create(
            user = user,
            beneficiary = benef_categiory,
        )


        
  