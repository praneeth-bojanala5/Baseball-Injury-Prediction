import statcast_raw
import statcast_clean
import fangraphs_raw
import fangraphs_clean
import precedes_injury


statcast_raw.statcast_raw()
statcast_clean.statcast_clean()
fangraphs_raw.fangraphs_raw()
fangraphs_clean.fangraphs_clean()
precedes_injury.injuries_to_df()
