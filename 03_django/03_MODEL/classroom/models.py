from django.db import models

# 1 model class : 1DB table 
class Student(models.Model):
    name = models.CharField(max_length= 10)
    age = models.IntegerField()
    major = models.CharField(max_length = 20)
    # CharField 함수는 max_length가 필요함
    # column 수정
    phone = models.TextField()

    def __str__(self):
        return f'({self.pk} => {self.name})'

class Product(models.Model):
    name = models.CharField(max_length= 200)
    price = models.IntegerField()
    year = models.CharField(max_length = 10)
    # CharField 함수는 max_length가 필요함
    # column 수정
    quantity = models.IntegerField()


# if __name__ == '__main__':
#     # CRUD operations
#     # 생성 Create
#     s1 = Student()
#     s1.name  = '권세훈'
#     s1.age = 20
#     s1.major = '산업공학과'
#     s1.phone = '01065681051'
#     s1.save() # 저장

#     s2 = Student(name='권세훈', age='40', major='기계', phone='010123456789')
#     s2.save()

#     Student.objects.create(name='권영우',age = '27', major='미대', phone='1234124214')
    
#     # 조회 Read/Retrieve
#         # 전체조회
#     Student.objects.all()
#         # 단일조회 (id==1)
#     Student.objects.get(pk=1)
#         # 레코드의 컬럼별 조회
#     s1.name
#     s1.age
#     s1.major
    
#     # 수정 Update => 모든 레코드의 모든 컬럼을 수정가능. id는 수정하지마라
#     s2 = Student.objects.get(pk=2)
#     s2.major = '경영학'
#     s2.save()
 
#     # 삭제 Delete
#     # '특정' 레코드를 선택하여 삭제한다
#     s3 = Student.objects.get(pk=3)
#     s3.delete()
 