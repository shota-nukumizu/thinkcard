# 開発環境

- Django 3.2.9
- Python 3.10.0
- Vue CLI 4.15.5
- Django REST FRAMEWORK
- Windows 11
- Visual Studio Code

# 初期設定

## 必要パッケージのインストール

コマンドプロンプトを開いてまずは以下のコマンドを入力する。

```powershell
django-admin startproject mysite .
django-admin startapp card
npm install -g @vue/cli
vue create vue-site
```

## Djangoの動作確認と基本設定

Djangoのインストールの確認は、以下のコマンドで確認できる。

```powershell
python manage.py runserver
```

`127.0.0.1:8000`(開発者用サーバ)にアクセスし、インストールが成功したら以下の画像が表示される。

`mysite/settings.py`を開いて、アプリ名と`rest_framework`を変数`INSTALLED_APPS`に加える。

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	#追加する部分
    'rest_framework',
    'card',
	#追加部分ここまで
]
```

## Vueの動作確認と基本設定

開発者用サーバの立ち上げは以下のコマンドで実行できる。

```powershell
cd vue-site
npm run serve
```

`localhost:8080`にアクセスし、インストールが成功したら以下の画面が表示される。

Vue CLIをインストールしたら、ディレクトリを移動させて以下のコマンドを入力する。

```powershell
cd vue-site
npm install axios
npm install toast
```

インストールする`axios`や`toast`はnodeのモジュールで、フロントエンドの見た目を整える時によく利用される。

### `axios`

PromiseベースのHTTP ClientライブラリでGETやPOSTのHTTPリクエストでサーバからのデータ取得やデータへのデータ送信を行う。

### `toast`

Vueで通知機能を実装する時に利用されるnpmライブラリ。

# データベースの作成

アイデアに入れる内容は以下の通り。

> * 投稿者名
* タイトル
* アイデア内容
* 投稿日時
* いいね数
* 発見
 

それぞれの内容を`card/models.py`に以下のように書き示す。

```python
from django.db import models

class IdeaModel(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=70)
    content = models.TextField()
    post_data = models.DateField(auto_now=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    interest = models.IntegerField(null=True, blank=True, default=0)
		
    #管理サイトに表示させるため
    def __str__(self):
        return self.title
```

以下のコマンドを入力してデータベース(`sqlite3.db`)を作成し、以下のコマンドを入力する。

```python
python manage.py makemigrations
python manage.py migrate
```

# `urls.py`のルーティング設定

まず最初に、`mysite/urls.py`を以下のように書き示す。

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('card.urls')),
]
```

次に、`card`フォルダに移動して、`api`フォルダと`urls.py`をそれぞれ作成する。

## `api`フォルダ内の処理

作成した`api`フォルダの中に以下のファイルを作成する。

> `__init__.py`：Pythonファイルをモジュールとして使えるようにするため

`serializer.py`：APIの設計をするため

`views.py`：開発者モードでAPIを閲覧できるようにするため
> 

それぞれ行った処理を順番に書いていく。

### `serializer.py`

`rest_framework`を使って以下のように記述する。

```python
from rest_framework import serializers
from card.models import IdeaModel

class IdeaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaModel
        fields = '__all__'
```

### `views.py`

```python
from rest_framework import generics
from card.models import IdeaModel
from .serializers import IdeaModelSerializer

class ListView(generics.ListCreateAPIView):
    queryset = IdeaModel.objects.all().order_by('-id') #降順に並べ替え
    serializer_class = IdeaModelSerializer

class DetailView(generics.RetrieveDestroyAPIView):
    queryset = IdeaModel.objects.all()
    serializer_class = IdeaModelSerializer
```

## `card/urls.py`の処理

`api`フォルダのコーディングが終了したら、`card/urls.py`を以下のように書き換える。

```python
from django.urls import path
from .api import views

urlpatterns = [
    path('idea/', views.ListView.as_view()),
    path('idea/<int:pk>', views.DetailView.as_view()),
]
```

これでルーティング設定は完了。

# 管理サイトへのアクセス

## `card/admin.py`の処理

該当ファイルに以下の処理を書き加える。

```python
from django.contrib import admin
from .models import IdeaModel

admin.site.register(IdeaModel)
```

## 管理者の作成

管理サイトにログインするためのサイト管理者を以下のコマンドで作成する。

```powershell
python manage.py createsuperuser
```

このコマンドを入力するとユーザ名とメールアドレス、パスワードを入力させられる。

開発者サーバで管理サイトにアクセスしてデータを作成し、`127.0.0.1:8000/idea`にアクセスすると、簡単ではあるがAPIを実装できる。(以下の画像を参照)

![2021-11-18](https://user-images.githubusercontent.com/82911032/142358068-aebba5e4-ac24-41ea-89b7-f46bc301dc1e.png)
