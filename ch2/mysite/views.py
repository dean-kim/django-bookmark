from django.views.generic.base import TemplateView


# TemplateView 제네릭 뷰를 상속받아 사용하고 있습니다. TemplateView를 사용하는 경우에는 필수적으로 template_name 클래스 변수를 오버라이딩으로 지정해줘야 합니다.
class HomeView(TemplateView):
    # mysite 프로젝트의 첫 화면을 보여주기 위한 템플릿 파일을 home.html로 지정했습니다. 템플릿 파일이 위치하는 디렉토리는 settings.py 파일의 TEMPLATE_DIR 항목으로 지정되어 있습니다.
    template_name = 'home.html'