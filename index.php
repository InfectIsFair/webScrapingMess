<html>

<head>

    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css"/>
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
    <py-env>
        - js
        - pyodide
    </py-env>

</head>

<body>

<main>

    <form onsubmit="return false">
        <select name="countries" id="countries">
            <option value="India">India</option>
            <option value="Germany">Germany</option>
            <option value="Netherlands">Netherlands</option>
        </select>

        <input type="submit" id="btn" pys-onClick="sub">


    </form> 

    <p>Output:</p>
    <p id='output'></p>

</main>

</body>

<footer>

    <py-script src="webScraping.py">
        card = cardDataMTG("Bladewing the Risen", "CMA", "175")
    </py-script>

    <py-script>
        from js import document
        from pyodide import create_proxy

        def sub(*args, **kwargs):
            global counter
            global card
            if (counter % 2) == 0:
                pyscript.write("output", "Hello")
            else:
                pyscript.write("output", "Goodbye")
            counter += 1
    
    </py-script>

</footer>

</html>