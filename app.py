from flask import Flask
AFI=Flask(__name__)
@AFI.route("/main")
def gangadhara():
    return '<center><h1> This Is Flask Statment......</h1></center>'

if __name__ == '__main__':
    AFI.run(debug=True)