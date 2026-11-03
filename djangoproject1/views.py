from django.http.response import HttpResponse


def main(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Раздел 1</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gradient-to-br from-indigo-50 via-slate-50 to-pink-50 min-h-screen flex items-center justify-center font-sans">
        <div class="max-w-md w-full bg-white shadow-xl rounded-2xl p-8 text-center border border-slate-100">
            <div class="inline-block p-3.5 bg-pink-50 text-pink-600 rounded-2xl mb-4 shadow-sm">
                <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                </svg>
            </div>
            <h1 class="text-3xl font-extrabold text-slate-800 tracking-tight">Раздел 1</h1>
            <p class="text-slate-500 mt-2">Добро пожаловать в мою личную визитку!</p>
            <div class="mt-6 flex justify-center gap-4">
                <a href="/bio" class="px-5 py-2.5 bg-indigo-600 text-white font-medium rounded-xl shadow-md hover:bg-indigo-700 transition duration-200">О себе</a>
                <a href="/facts" class="px-5 py-2.5 bg-slate-100 text-slate-700 font-medium rounded-xl hover:bg-slate-200 transition duration-200">Факты</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


def bio(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>О себе</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-50 min-h-screen flex items-center justify-center p-4 font-sans">
        <div class="max-w-xl w-full bg-white shadow-xl rounded-2xl p-8 border border-slate-100">
            <div class="flex items-center space-x-4 mb-6">
                <div class="p-3 bg-indigo-50 text-indigo-600 rounded-xl">
                    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                    </svg>
                </div>
                <div>
                    <h1 class="text-2xl font-bold text-slate-800">Карина</h1>
                    <span class="text-xs font-semibold text-indigo-600 bg-indigo-50 px-2.5 py-1 rounded-full uppercase tracking-wider">18 лет • Одесса → Бургас</span>
                </div>
            </div>

            <div class="text-slate-600 text-lg leading-relaxed bg-slate-50 p-6 rounded-xl border border-slate-100 space-y-4">
                <p>👋 Меня зовут <strong class="text-slate-800">Карина</strong>, мне <strong class="text-slate-800">18 лет</strong>.</p>
                <p>✈️ Я родилась в Одессе, а сейчас уже как <strong class="text-slate-800">5 лет</strong> живу в Бургасе.</p>
            </div>

            <div class="mt-8 flex justify-between items-center">
                <a href="/" class="text-sm font-medium text-slate-500 hover:text-slate-800 transition">← На главную</a>
                <a href="/facts" class="px-4 py-2 bg-indigo-600 text-white text-sm font-medium rounded-xl hover:bg-indigo-700 transition">Смотреть факты →</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


def facts(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Факты обо мне</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-50 min-h-screen flex items-center justify-center p-4 font-sans">
        <div class="max-w-xl w-full bg-white shadow-xl rounded-2xl p-8 border border-slate-100">
            <div class="flex items-center space-x-4 mb-6">
                <div class="p-3 bg-amber-50 text-amber-600 rounded-xl">
                    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"></path>
                    </svg>
                </div>
                <div>
                    <h1 class="text-2xl font-bold text-slate-800">Интересные факты</h1>
                    <span class="text-xs font-semibold text-amber-600 bg-amber-50 px-2.5 py-1 rounded-full uppercase tracking-wider">Обо мне</span>
                </div>
            </div>

            <div class="space-y-4">
                <div class="bg-gradient-to-r from-amber-50 to-orange-50 border border-amber-100 p-5 rounded-xl flex items-center space-x-4 shadow-sm">
                    <span class="text-3xl">🏆</span>
                    <p class="text-slate-700 font-medium">
                        Выиграла <strong class="text-amber-700 font-bold">100 евро</strong> в хакатоне!
                    </p>
                </div>

                <div class="bg-gradient-to-r from-blue-50 to-indigo-50 border border-blue-100 p-5 rounded-xl flex items-center space-x-4 shadow-sm">
                    <span class="text-3xl">🇨🇳</span>
                    <p class="text-slate-700 font-medium">
                        Знаю китайский язык на уровне <strong class="text-blue-700 font-bold">А2</strong>.
                    </p>
                </div>

                <div class="bg-gradient-to-r from-pink-50 to-purple-50 border border-pink-100 p-5 rounded-xl flex items-center space-x-4 shadow-sm">
                    <span class="text-3xl">🐱</span>
                    <p class="text-slate-700 font-medium">
                        Мой любимый маскот — милая кошечка <strong class="text-pink-700 font-bold">Пушин</strong>.
                    </p>
                </div>
            </div>

            <div class="mt-8 flex justify-between items-center">
                <a href="/" class="text-sm font-medium text-slate-500 hover:text-slate-800 transition">← На главную</a>
                <a href="/bio" class="px-4 py-2 bg-slate-800 text-white text-sm font-medium rounded-xl hover:bg-slate-700 transition">О себе →</a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)