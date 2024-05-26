from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        function = request.form['function']
        try:
            x, y = sp.symbols('x y')
            f = sp.sympify(function)

            df_dx = sp.diff(f, x)
            df_dy = sp.diff(f, y)
            d2f_dx2 = sp.diff(f, x, x)
            d2f_dy2 = sp.diff(f, y, y)
            d2f_dxdy = sp.diff(f, x, y)
            d2f_dydx = sp.diff(f, y, x)

            result = {
                'f': sp.pretty(f),
                'df_dx': sp.pretty(df_dx),
                'df_dy': sp.pretty(df_dy),
                'd2f_dx2': sp.pretty(d2f_dx2),
                'd2f_dy2': sp.pretty(d2f_dy2),
                'd2f_dxdy': sp.pretty(d2f_dxdy),
                'd2f_dydx': sp.pretty(d2f_dydx)
            }
        except Exception as e:
            result = {'error': str(e)}

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
