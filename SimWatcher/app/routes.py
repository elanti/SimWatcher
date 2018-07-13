from flask import render_template, request
from SimWatcher.app import app

computers = ['Piz Daint', 'Marconi']
simu = [['           1612746 knl_fua_p      source_LM_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1612747 knl_fua_p      source_LM_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1612749 knl_fua_p      source_LM_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1612751 knl_fua_p      source_LM_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1614751 knl_fua_p  source_square_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1614752 knl_fua_p  source_square_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1614753 knl_fua_p  source_square_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1614754 knl_fua_p  source_square_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1612744 knl_fua_p      source_LM_TCV_ITG_FD elanti00  R   19:51:53     64 r084c11s[01,04],r084c12s[02,04],r084c14s02,r084c15s[01,03],r084c17s03,r085c02s02,r085c05s03,r085c13s03,r085c14s04,r085c15s01,r085c16s[03-04],r085c18s03,r086c01s01,r086c02s04,r086c04s[03-04],r086c09s01,r086c10s03,r086c12s04,r086c14s04,r086c15s01,r086c16s04,r086c17s01,r086c18s03,r087c01s03,r087c03s[01,04],r087c10s01,r087c11s01,r087c12s03,r087c17s[01-02],r087c18s[01-02],r107c01s04,r107c02s04,r107c04s[01,04],r107c05s03,r107c06s04,r107c08s[01,03],r107c10s02,r107c11s04,r107c13s02,r107c14s[03-04],r107c16s[01-03],r107c18s04,r108c03s[02,04],r108c06s04,r108c10s03,r108c11s02,r108c13s03,r108c16s04,r108c17s[03-04]\n', '           1614750 knl_fua_p  source_square_TCV_ITG_FD elanti00  R   18:05:33     64 r084c11s[02-03],r084c12s03,r084c13s[01-03],r084c14s04,r084c15s04,r084c16s[01-04],r084c17s[01,04],r085c04s03,r085c06s[02-04],r085c07s01,r085c08s[03-04],r085c10s03,r085c11s03,r085c15s[03-04],r085c16s02,r086c01s[02-03],r086c02s03,r086c03s[01,04],r086c04s02,r086c05s04,r086c07s04,r086c09s04,r086c10s01,r086c13s[02,04],r086c15s[02,04],r086c17s02,r087c08s02,r087c13s02,r087c16s03,r087c17s04,r087c18s04,r107c03s04,r107c05s04,r107c08s04,r107c10s01,r107c12s[01-02,04],r107c15s02,r108c01s04,r108c04s02,r108c07s02,r108c09s[02,04],r108c10s04,r108c11s04,r108c13s01,r108c18s[01,03]\n'],['           1612746 knl_fua_p      source_LM_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1612747 knl_fua_p      source_LM_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1612749 knl_fua_p      source_LM_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1612751 knl_fua_p      source_LM_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1614751 knl_fua_p  source_square_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1614752 knl_fua_p  source_square_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1614753 knl_fua_p  source_square_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1614754 knl_fua_p  source_square_TCV_ITG_FD elanti00 PD       0:00     64 (Dependency)\n', '           1612744 knl_fua_p      source_LM_TCV_ITG_FD elanti00  R   19:51:53     64 r084c11s[01,04],r084c12s[02,04],r084c14s02,r084c15s[01,03],r084c17s03,r085c02s02,r085c05s03,r085c13s03,r085c14s04,r085c15s01,r085c16s[03-04],r085c18s03,r086c01s01,r086c02s04,r086c04s[03-04],r086c09s01,r086c10s03,r086c12s04,r086c14s04,r086c15s01,r086c16s04,r086c17s01,r086c18s03,r087c01s03,r087c03s[01,04],r087c10s01,r087c11s01,r087c12s03,r087c17s[01-02],r087c18s[01-02],r107c01s04,r107c02s04,r107c04s[01,04],r107c05s03,r107c06s04,r107c08s[01,03],r107c10s02,r107c11s04,r107c13s02,r107c14s[03-04],r107c16s[01-03],r107c18s04,r108c03s[02,04],r108c06s04,r108c10s03,r108c11s02,r108c13s03,r108c16s04,r108c17s[03-04]\n', '           1614750 knl_fua_p  source_square_TCV_ITG_FD elanti00  R   18:05:33     64 r084c11s[02-03],r084c12s03,r084c13s[01-03],r084c14s04,r084c15s04,r084c16s[01-04],r084c17s[01,04],r085c04s03,r085c06s[02-04],r085c07s01,r085c08s[03-04],r085c10s03,r085c11s03,r085c15s[03-04],r085c16s02,r086c01s[02-03],r086c02s03,r086c03s[01,04],r086c04s02,r086c05s04,r086c07s04,r086c09s04,r086c10s01,r086c13s[02,04],r086c15s[02,04],r086c17s02,r087c08s02,r087c13s02,r087c16s03,r087c17s04,r087c18s04,r107c03s04,r107c05s04,r107c08s04,r107c10s01,r107c12s[01-02,04],r107c15s02,r108c01s04,r108c04s02,r108c07s02,r108c09s[02,04],r108c10s04,r108c11s04,r108c13s01,r108c18s[01,03]\n']]
sim = []
for s in simu:
    p = []
    for param in s:
        params = param.split()
        p.append(params)
    sim.append(p)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/my_simulations', methods=('GET', 'POST'))
def my_simulations():
    return render_template(
        'my_simulations.html',
        simulations=sim,
        computers=computers,
    )
