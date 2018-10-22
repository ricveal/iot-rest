⚠️ UNMAINTAINED ⚠️

Backend and Sensor Sketch to config a RESTful API that connects the info from the sensor (Arduino) with an SQL Database (In this example SQLITE).

## Installation

```bash
pip install -r /path/to/requirements.txt
```

## Configuration

For create and config the DB, open a Python interpreter and execute:

```python
from app import db
from sensor import Sensor
db.create_all()
```

## Authors / Autores

* **Ricardo Vega** - [ricveal](http://ricveal.com)

## License / Licencia

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

Este proyecto está licenciado bajo un licencia MIT - Puedes ver el archivo [LICENSE.md](LICENSE.md) para más detalles

