from django.http.response import HttpResponse
from django.templatetags.static import static

def main(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Раздел 2</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gradient-to-br from-slate-50 to-slate-100 min-h-screen flex items-center justify-center font-sans">
        <div class="max-w-md w-full bg-white shadow-xl rounded-2xl p-8 text-center border border-slate-100">
            <div class="inline-block p-3 bg-indigo-50 text-indigo-600 rounded-xl mb-4">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
                </svg>
            </div>
            <h1 class="text-3xl font-extrabold text-slate-800 tracking-tight">Раздел 2</h1>
            <p class="text-slate-500 mt-2">Добро пожаловать в путеводитель по Бургасу.</p>
            <div class="mt-6 flex justify-center gap-4">
                <a href="/api/info" class="px-5 py-2.5 bg-indigo-600 text-white font-medium rounded-xl shadow-md hover:bg-indigo-700 transition duration-200">О городе</a>
                <a href="/api/places" class="px-5 py-2.5 bg-slate-100 text-slate-700 font-medium rounded-xl hover:bg-slate-200 transition duration-200">Достопримечательности</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


def info(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>О Бургасе</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-50 min-h-screen flex items-center justify-center p-4 font-sans">
        <div class="max-w-xl w-full bg-white shadow-xl rounded-2xl p-8 border border-slate-100">
            <div class="flex items-center space-x-4 mb-6">
                <div class="p-3 bg-blue-50 text-blue-600 rounded-xl">
                    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                    </svg>
                </div>
                <div>
                    <h1 class="text-2xl font-bold text-slate-800">О городе Бургас</h1>
                    <span class="text-xs font-semibold text-blue-600 bg-blue-50 px-2.5 py-1 rounded-full uppercase tracking-wider">Болгария</span>
                </div>
            </div>
            <p class="text-slate-600 text-lg leading-relaxed bg-slate-50 p-6 rounded-xl border border-slate-100">
                Бургас находится на юге Болгарии у моря. Это прекрасный портовый и культурный центр с живописными пляжами и знаменитым Морским парком.
            </p>
            <div class="mt-8 flex justify-between items-center">
                <a href="/api" class="text-sm font-medium text-slate-500 hover:text-slate-800 transition">← На главную</a>
                <a href="/api/places" class="px-4 py-2 bg-blue-600 text-white text-sm font-medium rounded-xl hover:bg-blue-700 transition">Смотреть места →</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


def places(request):
    img1 = static('imgs/5427140385290526542_121.jpg')
    img2 = static('imgs/5427140385290526541_121.jpg')
    img3 = static('imgs/5427140385290526543_121.jpg')

    html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Достопримечательности Бургаса</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-50 min-h-screen py-12 px-4 font-sans">
        <div class="max-w-6xl mx-auto">
            <div class="text-center mb-10">
                <h1 class="text-3xl font-extrabold text-slate-800 tracking-tight">Достопримечательности города</h1>
                <p class="text-slate-500 mt-2">Лучшие моменты и кадры Бургаса</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-white rounded-2xl shadow-lg p-6 border border-slate-100 flex flex-col justify-between">
                    <p class="text-slate-700 font-medium text-center mb-4 text-lg">Котики</p>
                    <div class="aspect-square w-full rounded-xl overflow-hidden shadow-inner bg-slate-100 group">
                        <img src="{img1}" 
                             alt="Котики" 
                             class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                </div>

                <div class="bg-white rounded-2xl shadow-lg p-6 border border-slate-100 flex flex-col justify-between">
                    <p class="text-slate-700 font-medium text-center mb-4 text-lg">Медвед</p>
                    <div class="aspect-square w-full rounded-xl overflow-hidden shadow-inner bg-slate-100 group">
                        <img src="{img2}" 
                             alt="Медвед" 
                             class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                </div>

                <div class="bg-white rounded-2xl shadow-lg p-6 border border-slate-100 flex flex-col justify-between">
                    <p class="text-slate-700 font-medium text-center mb-4 text-lg">Прикольный мост</p>
                    <div class="aspect-square w-full rounded-xl overflow-hidden shadow-inner bg-slate-100 group">
                        <img src="{img3}" 
                             alt="Прикольный мост" 
                             class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    </div>
                </div>
            </div>

            <div class="mt-10 text-center">
                <a href="/api" class="inline-block px-6 py-2.5 bg-slate-800 text-white font-medium rounded-xl shadow hover:bg-slate-700 transition">← На главную</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)