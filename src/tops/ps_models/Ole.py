def load():
    return{
        'base_mva': 500,
        'f': 50,
        'slack_bus': '1',

        'buses': [
            ['name', 'V_n'],
            ['1', 16.5],
            ['2', 16,5],
        ],

        'lines': [
            ['name', 'from_bus', 'to_bus', 'length', 'V_n', 'unit', 'R', 'X', 'B'],
            ['L1-2', '1', '2', 100, 16.5, 'pf', 0.02554745, 0.3, 3.599926],
        ],

        'loads': [
            ['name', 'bus', 'P', 'Q', 'model'],
            ['L2', '2', 20, 1, 'Z'],
        ],

        'generators': {
            'GEN': [
                ['name', 'bus', 'S_n', 'V_n', 'PF_n', 'P', 'V', 'N_par', 'H', 'D', 'X_d', 'X_q', 'X_d_t', 'X_q_t', 'X_d_st', 'X_q_st', 'T_d0_t', 'T_q0_t', 'T_d0_st', 'T_q0_st'],
                ['G1', '39', 10000, 345., 0.85, 1000., 1.03, 1, 5., 0, 2., 1.9, 0.6, 0.8, 0.4, 0.4, 7., 0.7, 0.05, 0.035],
            ]
        }
    }