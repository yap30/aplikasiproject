from django.http import HttpResponse
from django.template import loader
# Create your views here.
def beranda(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

#latihan
def profile(request):
    return HttpResponse("Halo ini tulisan dari profile")

def rekomendasi(request):
    template = loader.get_template('rekomendasi.html')
    return HttpResponse(template.render())

def reservasi_kunjungan(request):
    template = loader.get_template('reservasi_kunjungan.html')
    return HttpResponse(template.render())
