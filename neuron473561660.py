'''
Defines a class, Neuron473561660, of neurons from Allen Brain Institute's model 473561660

A demo is available by running:

    python -i mosinit.py
'''
class Neuron473561660:
    def __init__(self, name="Neuron473561660", x=0, y=0, z=0):
        '''Instantiate Neuron473561660.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron473561660_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Rorb-IRES2-Cre-D_Ai14_IVSCC_-171056.05.01.01_470521767_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron473561660_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 100.0
            sec.e_pas = -82.6876653035
        
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000759461803864
        for sec in self.dend:
            sec.cm = 1.0
            sec.g_pas = 0.000200030582037
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.00685129
            sec.gbar_Ih = 1.59635e-05
            sec.gbar_NaTs = 0.243367
            sec.gbar_Nap = 0.000164535
            sec.gbar_K_P = 0
            sec.gbar_K_T = 0
            sec.gbar_SK = 0.000900349
            sec.gbar_Kv3_1 = 0.00270852
            sec.gbar_Ca_HVA = 0.000489083
            sec.gbar_Ca_LVA = 0.00630378
            sec.gamma_CaDynamics = 0.000889512
            sec.decay_CaDynamics = 477.172
            sec.g_pas = 0.000831418
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

