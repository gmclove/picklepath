from picklePath import PicklePath as PP

class TestPath(PP):
    def __init__(self, run_path='default_run',
                 *args, **kwargs
                 ):
        #####################################
        #    Default/Optional Attributes    #
        #####################################
        ### Optimization Pre/Post Processing ###
        # self.n_opt = int(n_opt)
        # self.gens_per_plot = int(gens_per_plot)
        ##########################
        #    Pickle Path Init    #
        ##########################
        super().__init__(dir_path=run_path)
        self.run_path = self.abs_path
        self.logger.info(f'OPTIMIZATION STUDY- {self.rel_path}')
        self.logger.info(f'\tCheckpoint Path: {self.cp_path}')
        if self.cp_init:
            return
        #######################################
        #    ATTRIBUTES NEEDED FOR RESTART    #
        #######################################
