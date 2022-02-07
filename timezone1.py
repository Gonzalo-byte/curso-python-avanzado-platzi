from datetime import datetime
import pytz

buenos_aires_timezone = pytz.timezone("America/Argentina/Buenos_Aires")
bsas_date = datetime.now(buenos_aires_timezone)
print(f"Día y hora BS AS:  {bsas_date.strftime('%d/%h/%Y  -  %H-%M-%S')}")