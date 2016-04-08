from pybrain.structure import FeedForwardNetwork
from pybrain.structure import FullConnection
from pybrain.structure import SigmoidLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import numpy as np

class RNA:
    def __init__(self):
        self.red = FeedForwardNetwork()
        self.error_minimo = 0.01
        self.inputs = 0
        self.outputs = 0

    def configurar_RNA(self):
        self.inLayer = SigmoidLayer(42)
        self.hiddenLayer = SigmoidLayer(10)
        self.outLayer = SigmoidLayer(6)

        self.red.addInputModule(self.inLayer)
        self.red.addModule(self.hiddenLayer)
        self.red.addOutputModule(self.outLayer)

        self.in_to_hidden = FullConnection(self.inLayer,self.hiddenLayer)
        self.hidden_to_out = FullConnection(self.hiddenLayer,self.outLayer)

        self.red.addConnection(self.in_to_hidden)
        self.red.addConnection(self.hidden_to_out)
        self.red.sortModules()

    def ver_confi(self):
        print self.red

    def ver_pesos(self):
        print self.in_to_hidden.params
        print self.hidden_to_out.params

    def leer_archivo(self, nombre):
        f = open(nombre)

        for linea in f:
            linea = np.array(linea.split()).astype(int)
            self.inputs = np.array(linea[:-6])
            self.outputs = np.array(linea[-6:])

    def entrenamiento(self):
        ds = SupervisedDataSet(42, 6)
        ds.addSample(self.inputs, self.outputs)

        trainer = BackpropTrainer(self.red, ds)
        error = trainer.train()
        print error

        while error > self.error_minimo:
            error = trainer.train()
            print error


neurona = RNA()
neurona.configurar_RNA()
#neurona.verConfi()
#neurona.verPesos()
neurona.leer_archivo("datos.txt")
neurona.entrenamiento()
#neurona.ver_pesos()