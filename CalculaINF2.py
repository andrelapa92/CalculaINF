from ui_calc4 import *
from ui_config_win import *
from PySide2 import QtWidgets
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
import json


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)


class Conf(QtWidgets.QMainWindow, Ui_configWindow):
    def __init__(self):
        super(Conf, self).__init__()
        self.setupUi(self)
        appIcon2 = QIcon("icon.png")
        self.setWindowIcon(appIcon2)


def abrir_conf():
    config.show()


def main(ui):

    anosemestre = ui.spinBox
    data_referencia = config.date_refer
    primeira_turma = config.t_pri
    result_primeira_turma = config.r_pri
    segunda_turma = config.t_seg
    result_segunda_turma = config.r_seg
    terceira_turma = config.t_ter
    result_terceira_turma = config.r_ter
    quarta_turma = config.t_qua
    result_quarta_turma = config.r_qua

    def carregar_config():
        if os.path.exists('configuracoes.json'):
            with open('configuracoes.json', 'r', encoding='utf-8') as f:
                configuracoes = json.load(f)
                anosemestre.setValue(int(configuracoes["anosemestre"]))
                data_split = configuracoes["data_referencia"].split('/')
                dia_ref = int(data_split[0])
                mes_ref = int(data_split[1])
                data_referencia.setDate(QDate(2021, mes_ref, dia_ref))
                primeira_turma.setText(configuracoes["primeira_turma"])
                result_primeira_turma.setText(configuracoes["result_primeira_turma"])
                segunda_turma.setText(configuracoes["segunda_turma"])
                result_segunda_turma.setText(configuracoes["result_segunda_turma"])
                terceira_turma.setText(configuracoes["terceira_turma"])
                result_terceira_turma.setText(configuracoes["result_terceira_turma"])
                quarta_turma.setText(configuracoes["quarta_turma"])
                result_quarta_turma.setText(configuracoes["result_quarta_turma"])
                return configuracoes

    def calc():
        matricula = anosemestre.text()
        nasc = ui.dateEdit.text()
        ref = data_referencia.text()+"/"
        a = nasc
        b = ref + matricula
        f = '%d/%m/%Y'
        ini = datetime.strptime(a, f)
        fim = datetime.strptime(b, f)
        di = abs(relativedelta(ini, fim))

        ano = ''
        mes = ''
        dia = ''

        if di.years > 1:
            ano = 'anos'
        else:
            ano = 'ano'
        if di.months > 1:
            mes = 'meses'
        else:
            mes = 'mês'
        if di.days > 1:
            dia = 'dias'
        else:
            dia = 'dia'
        
        if str(di.years) == result_primeira_turma.text():
            ui.listWidget.clear()
            ui.listWidget.addItem(config.t_pri.text())
            ui.label_4.setText(f'{di.years} {ano}, {di.months} {mes} e {di.days} {dia}')
            ui.label_4.setHidden(False)

        elif str(di.years) == result_segunda_turma.text():
            ui.listWidget.clear()
            ui.listWidget.addItem(config.t_seg.text())
            ui.label_4.setText(f'{di.years} {ano}, {di.months} {mes} e {di.days} {dia}')
            ui.label_4.setHidden(False)

        elif str(di.years) == result_terceira_turma.text():
            ui.listWidget.clear()
            ui.listWidget.addItem(config.t_ter.text())
            ui.label_4.setText(f'{di.years} {ano}, {di.months} {mes} e {di.days} {dia}')
            ui.label_4.setHidden(False)

        elif str(di.years) == result_quarta_turma.text():
            ui.listWidget.clear()
            ui.listWidget.addItem(config.t_qua.text())
            ui.label_4.setText(f'{di.years} {ano}, {di.months} {mes} e {di.days} {dia}')
            ui.label_4.setHidden(False)

        elif di.years < 2:
            ui.listWidget.clear()
            ui.listWidget.addItem("Ainda não atingiu a idade mínima.")
            ui.label_4.setText(f'{di.years} {ano}, {di.months} {mes} e {di.days} {dia}')
            ui.label_4.setHidden(False)

        else:
            ui.listWidget.clear()
            ui.listWidget.addItem("Idade incompatível com Ensino Infantil.")
            ui.label_4.setText(f'{di.years} {ano}, {di.months} {mes} e {di.days} {dia}')
            ui.label_4.setHidden(False)

    def salvar_conf():
        with open('configuracoes.json', 'w') as f:
            configuracoes = {
                "anosemestre": anosemestre.text(),
                "data_referencia": data_referencia.text(),
                "primeira_turma": primeira_turma.text(),
                "result_primeira_turma": result_primeira_turma.text(),
                "segunda_turma": segunda_turma.text(),
                "result_segunda_turma": result_segunda_turma.text(),
                "terceira_turma": terceira_turma.text(),
                "result_terceira_turma": result_terceira_turma.text(),
                "quarta_turma": quarta_turma.text(),
                "result_quarta_turma": result_quarta_turma.text()
            }
            json.dump(configuracoes, f)
        config.close()

    ui.pushButton.clicked.connect(calc)
    ui.pushButton.clicked.connect(salvar_conf)
    ui.toolButton.clicked.connect(abrir_conf)
    config.botao_salvar.clicked.connect(salvar_conf)
    carregar_config()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    config = Conf()
    main(ui)
    ui.show()
    sys.exit(app.exec_())
