import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def fill_dd(self):
        options_biblioteche = [ft.DropdownOption(key="Nessun filtro", text="Nessun filtro")]
        for b in self._model.get_biblioteche():
            options_biblioteche.append(ft.DropdownOption(key=b.nome, text=b.nome))

        options_generi = [ft.DropdownOption(key="Nessun filtro", text="Nessun filtro")]
        for g in self._model.get_generi():
            if g:
                options_generi.append(ft.DropdownOption(key=g, text=g))

        self._view.dd_biblioteca.options = options_biblioteche
        self._view.dd_genere.options = options_generi

        self._view.dd_biblioteca.update()
        self._view.dd_genere.update()

    # CALLBACKS DROPDOWN
    def leggi_biblioteca(self, e):
        self.biblioteca_selezionata = e.control.value
    def leggi_genere(self, e):
        self.genere_selezionato = e.control.value

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        biblioteca = self._view.dd_biblioteca.value
        genere = self._view.dd_genere.value
        libri = self._model.get_libri_filtrati(biblioteca, genere)
        self._view.list_view_libri.controls.clear()

        if not libri:
            self._view.show_alert("Nessun libro trovato con i filtri selezionati.")
        else:
            self._view.list_view_libri.controls.append(ft.Text(f"Totale libri trovati: {len(libri)}"))
            for libro in libri:
                self._view.list_view_libri.controls.append(ft.Text(str(libro)))
        self._view.update()
