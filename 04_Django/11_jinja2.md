### 1.安装 jinja2 模块

```
    pip install jinja2
```

### 2.Django 配置 jinja2

1. 在项目文件中创建 jinja2_env.py 文件

```
from jinja2 import Environment

def environment(**options):
    env = Environment(**options)

    return env
```

2.在 settings.py 文件

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',#修改1
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS':True,
        'OPTIONS':{
            'environment': 'jinja2_env.environment',# 修改2
            'context_processors':[
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 3.jinja2 模板的使用绝大多数和 Django 自带模板一样

```
1.for循环有差异
```

### 4.jinja2 自定义过滤器

#### 在 jinja2_env.py 文件中自定义过滤器

```
from jinja2 import Environment

def environment(**options):
    env = Environment(**options)

    # 2.将自定义的过滤器添加到 环境中
    env.filters['do_listreverse'] = do_listreverse

    return env

# 1.自定义过滤器
def do_listreverse(li):
    if li == "B":
        return "哈哈"
```