from django.shortcuts import render
from django.views import View
from .utils import make_api_request

class PrevisaoTempoView(View):
    def get(self, request):
        cidade_padrao = 'Milan'  # Definir a cidade padrão como Milão, Itália
        dados_previsao_tempo = self.obter_previsao_tempo(cidade_padrao)
        return render(request, 'meteocast/previsao_tempo1.html', {'previsao_tempo1': dados_previsao_tempo})

    def obter_previsao_tempo(self, cidade):
        api_key = '8197995a86d1d31479e30ec445ed6635' # Chave da API OpenWeatherMap
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric'

        data = make_api_request(api_key, url)
        if data:
            previsao_tempo = {
                'cidade': cidade,
                'temperatura': data['main']['temp'],
                'condicao': data['weather'][0]['description'].capitalize()
            }
            return previsao_tempo
        else:
            return None




