from api.models import User, Report, ImageReport, Comment
from api.serializers import UserSerializer, ReportSerializer, ImageReportSerializer, CommentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

user = User(name='Horacio', email='horacio@gmail.com', password='ska', profile_picture='api/media/profile_pic.png')
user.save()

#get id
report = Report(user_fk=user, name_subject='Antonio Campos', status='encontrado', gender='masculino', birth_date='1993-02-02', state='Nayarit', city='San Blas', missing_date='2014-04-02', description='Le encanta la polla al mojo de ajo')
report.save()

imageReport = ImageReport(report_fk=report, image='api/media/default/missing_pic.png')
imageReport.save()

comment = Comment(report_fk=report, comment_date='2014-04-02', content='Me encontre un calcetin mojado')
comment.save()

userSerializer = UserSerializer(user)
userSerializer.data

rs = ReportSerializer(report)
rs.data

irs = ImageReportSerializer(imageReport)
irs.data

cs = CommentSerializer(comment)
cs.data

content = JSONRenderer().render(userSerializer.data)
content

contentReport = JSONRenderer().render(rs.data)
contentReport

contentImageReport = JSONRenderer().render(irs.data)
contentImageReport

contentComment = JSONRenderer().render(cs.data)
contentComment

#Deserialize User
from django.utils.six import BytesIO

stream = BytesIO(content)
data = JSONParser().parse(stream)

serializer = UserSerializer(data=data)

#Deserialize Report
stream = BytesIO(contentReport)
data = JSONParser().parse(stream)

serializer = ReportSerializer(data=data)

#Deserialize ImageReport
stream = BytesIO(contentImageReport)
data = JSONParser().parse(stream)

serializer = ImageReportSerializer(data=data)

#Deserialize Comment
stream = BytesIO(contentComment)
data = JSONParser().parse(stream)

serializer = CommentSerializer(data=data)



#Check generic valid
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()

