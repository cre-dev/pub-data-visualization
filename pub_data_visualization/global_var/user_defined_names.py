
"""
    User defined names to format data coming from different sources.
    
"""

import pandas as pd

### Auctions
auction_company        = 'auction day-ahead'
auction_dt_local       = 'auction_dt (local)'
auction_dt_UTC         = 'auction_dt (UTC)'
auction_price_euro_mwh = 'auction price (€/MWh)'
auction_pricing        = 'auction pricing'
auction_power_mw       = 'auction power (MW)'
auction_volume_mwh     = 'auction volume (MWh)'

### Brokers
broker_id        = 'broker_id'
broker_long_name = 'broker_long_name'
broker_name      = 'broker_name'

### Capacities
capacity_day_UTC        = 'capacity day (UTC)'
capacity_dt_UTC         = 'capacity_dt (UTC)'
capacity_end_date_local = 'capacity_end_date (local)'
capacity_end_date_UTC   = 'capacity_end_date (UTC)'
capacity_flag_deleted   = 'capacity_flag_deleted'
capacity_month_UTC      = 'capacity month (UTC)'
capacity_gw             = 'capacity (GW)'
capacity_mw             = 'capacity (MW)'
capacity_year_UTC       = 'capacity year (UTC)'

### Commodities
commodity             = 'commodity'
commodity_electricity = 'EL'
commodity_gas         = 'NG'

### Companies (Trading)
company_id           = 'company_id'
company_name         = 'company_name'
company_name_info    = 'company_name_info'
company_name_unknown = 'company_unknown'

### Contracts
contract                                = 'contract'
contract_code                           = 'contract_code'
contract_delivery_begin_date_local      = 'delivery_begin_date (local)'
contract_delivery_begin_date_UTC        = 'delivery_begin_date (UTC)'
contract_delivery_begin_day_local       = 'delivery_begin_day (local)'
contract_delivery_begin_day_UTC         = 'delivery_begin_day (UTC)' # used for spot auctions entsoe
contract_delivery_begin_dt_local        = 'delivery_begin_dt (local)'
contract_delivery_begin_dt_unknown      = pd.NaT
contract_delivery_begin_dt_UTC          = 'delivery_begin_dt (UTC)'
contract_delivery_begin_hour_local      = 'delivery_begin_hour (local)'
contract_delivery_begin_month_local     = 'delivery_begin_month (local)'
contract_delivery_begin_month_UTC       = 'delivery_begin_month (UTC)'
contract_delivery_begin_year_local      = 'delivery_begin_year (local)'
contract_delivery_begin_year_unknown    = -1
contract_delivery_begin_year_UTC        = 'delivery_begin_year (UTC)'
contract_delivery_end_date_local        = 'delivery_end_date (local)'
contract_delivery_end_date_UTC          = 'delivery_end_date (UTC)'
contract_delivery_end_date_unknown      = pd.NaT
contract_delivery_end_dt_local          = 'delivery_end_dt (local)'
contract_delivery_end_dt_UTC            = 'delivery_end_dt (UTC)'
contract_delivery_end_hour_local        = 'delivery_end_hour (local)'
contract_delivery_nb_hours              = 'delivery_nb_hours'
contract_delivery_period_index          = 'delivery_period_index'
contract_delivery_period_index_bloc              = '{month:0>2}{day:0>2}{hour_begin:0>2}{hour_end:0>2}'
contract_delivery_period_index_bloc_pattern      = r"^(\d{1,2})(\d{2})(\d{2})(\d{2})$"
contract_delivery_period_index_bom               = '{month:0>2}{day:0>2}'
contract_delivery_period_index_bow               = '{month:0>2}{day:0>2}'
contract_delivery_period_index_days              = '{month:0>2}{day:0>2}{nb_days:0>2}'
contract_delivery_period_index_days_pattern      = r"^(\d{1,2})(\d{2})(\d{2})$"
contract_delivery_period_index_day               = '{month:0>2}{day:0>2}'
contract_delivery_period_index_day_pattern       = r"^(\d{1,2})(\d{2})$"
contract_delivery_period_index_half_hour         = '{month:0>2}{day:0>2}{hour:0>2}{minute:0>2}'
contract_delivery_period_index_half_hour_pattern = r"^(\d{1,2})(\d{2})(\d{2})(\d{2})$"
contract_delivery_period_index_hour              = '{month:0>2}{day:0>2}{hour:0>2}'
contract_delivery_period_index_hour_pattern      = r"^(\d{1,2})(\d{2})(\d{2})$"
contract_delivery_period_index_gas_year          = 1
contract_delivery_period_index_months            = '{month:0>2}{nb_months:0>2}'
contract_delivery_period_index_NA                = 0
contract_delivery_period_index_summer            = 1
contract_delivery_period_index_unknown           =-1
contract_delivery_period_index_week              = '{month:0>2}{day:0>2}'
contract_delivery_period_index_week_pattern      = r"^(\d{1,2})(\d{2})$"
contract_delivery_period_index_weekbgn           = '{month:0>2}{day:0>2}'
contract_delivery_period_index_weekbgn_pattern   = r"^(\d{1,2})(\d{2})$"
contract_delivery_period_index_weekend           = '{month:0>2}{day:0>2}'
contract_delivery_period_index_weekend_pattern   = r"^(\d{1,2})(\d{2})$"
contract_delivery_period_index_winter            = 2
contract_delivery_period_index_year              = 1
contract_delivery_period_index_years             = '{nb_years}'
contract_delivery_type                  = 'delivery_type'
contract_delivery_tz                    = 'contract_delivery_tz'
contract_delivery_windows               = 'contract_delivery_windows'
contract_delivery_zone                  = 'contract_delivery_zone'
contract_delivery_zone_spread           = 'zone_spread'
contract_delivery_zone_unknown          = 'unknown'
contract_frequency                      = 'frequency'
contract_frequency_info                 = 'frequency_info'
contract_frequency_type                 = 'frequency_type'
contract_frequency_bloc                 = 'BLOC'
contract_frequency_bom                  = 'BOM'
contract_frequency_boq                  = 'BOQ'
contract_frequency_bos                  = 'BOS'
contract_frequency_bow                  = 'BOW'
contract_frequency_boy                  = 'BOY'
contract_frequency_gas_day              = 'GD'
contract_frequency_day                  = 'D'
contract_frequency_days                 = 'Ds'
contract_frequency_gas_year             = 'GY'
contract_frequency_half_hour            = 'HALFH'
contract_frequency_hour                 = 'H'
contract_frequency_month                = 'M'
contract_frequency_months               = 'Ms'
contract_frequency_quarter              = 'Q'
contract_frequency_season               = 'S'
contract_frequency_spread               = 'SPREAD?'
contract_frequency_unknown              = 'frequency_unknown'
contract_frequency_week                 = 'W'
contract_frequency_weekbgn              = 'WD'
contract_frequency_weekend              = 'WE'
contract_frequency_year                 = 'Y'
contract_frequency_years                = 'Ys'
contract_info                           = 'contract_info'
contract_instrument                     = 'instrument'
contract_instrument_type                = 'instrument_type'
contract_is_option                      = 'is_option'
contract_is_option_true                 = 1
contract_is_option_false                = 0
contract_is_option_unknown              = -1
contract_is_spread                      = 'is_spread'
contract_is_spread_true                 = 1
contract_is_spread_false                = 0
contract_is_spread_unknown              = -1
contract_is_swap                        = 'is_swap'
contract_is_swap_true                   = 1
contract_is_swap_false                  = 0
contract_is_swap_unknown                = -1
contract_name                           = 'contract_name'
contract_nature                         = 'contract_nature'
contract_profile                        = 'profile'
contract_profile_base                   = 'BASE'
contract_profile_bloc                   = 'BLOC.{hour_begin}.{hour_end}'
contract_profile_bloc_pattern           = r"BLOC.(\d{1,2}).(\d{1,2}).*$"
contract_profile_gas                    = 'GAS'
contract_profile_hour                   = contract_frequency_hour
contract_profile_half_hour              = contract_frequency_half_hour
contract_profile_info                   = 'profile_info'
contract_profile_NA                     = 'NA'
contract_profile_ofpk                   = 'OFPK'
contract_profile_peak                   = 'PEAK'
contract_profile_spread                 = 'SPREAD?'
contract_profile_unknown                = 'profile_unknown'
contract_profile_wday1620               = 'WD1620'
contract_profile_wday2024               = 'WD2024'
contract_profile_wend                   = 'WEND?'
contract_profile_wend2024               = 'WE2024'
contract_settlement_type                = 'settlement_type'
contract_volume_mwh                     = 'contract_volume (MWh)'
contract_volume_impacted_mwh            = 'contract_volume_impacted (MWh)'

### Currencies
currency          = 'currency'
currency_per_unit = 'currency_per_unit'

### Data sources
data_source_auctions            = 'data_source_auctions'
data_source_auctions_entsoe     = 'ENTSO-E'
data_source_capacity            = 'data_source_capacity'
data_source_capacity_entsoe     = 'ENTSO-E'
data_source_capacity_rte        = 'RTE'
data_source_indices             = 'data_source_indices'
data_source_load                = 'data_source_load'
data_source_load_eco2mix        = 'eCO2mix'
data_source_load_entsoe         = 'ENTSOE'
data_source_orders              = 'data_source_orders'
data_source_outages             = 'data_source_outages'
data_source_outages_rte         = 'RTE'
data_source_outages_entsoe      = 'ENTSO-E'
data_source_production          = 'data_source_production'
data_source_production_eco2mix  = 'eCO2mix'
data_source_production_entsoe   = 'ENTSOE'
data_source_production_rte      = 'RTE'
data_source_trades              = 'data_source_trades'
data_source_weather             = 'data_source_weather'
data_source_weather_meteofrance = 'MétéoFrance'

### Files
file_info   = 'file_info'
file_name   = 'file_name'
file_source = 'file_source'

### Geography
geography_area_code                   = 'area_code'
geography_area_name                   = 'area_name'
geography_area_name_second            = 'area_name_second'
geography_area_type_code              = 'area_type_code'
geography_coordinates                 = 'coordinates'
geography_country                     = 'country'
geography_latitude                    = 'latitude'
geography_longitude                   = 'longitude'
geography_map_code                    = 'map_code'
geography_map_code_belgium            = 'BE'
geography_map_code_france             = 'FR'
geography_map_code_gb                 = 'GB'
geography_map_code_germany            = 'DE'
geography_map_code_germany_luxembourg = 'DE'
geography_map_code_italy              = 'IT'
geography_map_code_netherlands        = 'NL'
geography_map_code_portugal           = 'PT'
geography_map_code_spain              = 'SP'
geography_map_code_swiss              = 'CH'
geography_map_code_uk                 = 'UK'
geography_map_code_unknown            = 'map_code_unknown'
geography_zone_france                 = 'metropolitan_France'

### Indices
index_date_local               = 'index date (local)'
index_date_UK                  = 'index date (UK)'
index_date_UTC                 = 'index date (UTC)'
index_dt_local                 = 'index dt (local)'
index_dt_UK                    = 'index dt (UK)'
index_dt_UTC                   = 'index dt (UTC)'
index_id                       = 'index_id'
index_nb_trades                = 'nb_trades'
index_nb_trades_non_mtf        = 'nb_trades_non_mtf'
index_nb_trades_otc            = 'nb_trades_otc'
index_nb_trades_reg            = 'nb_trades_trade_regist'
index_nb_contracts             = 'nb_contracts'
index_nb_contracts_non_mtf     = 'nb_contracts_non_mtf'
index_nb_contracts_otc         = 'nb_contracts_otc'
index_nb_contracts_traded_reg  = 'nb_contracts_trade_reg'
index_open_interest_contracts  = 'index_open_interest_contracts'
index_open_interest_volume_mwh = 'index_open_interest_volume (MWh)'
index_open_price_euro_mwh      = 'index_open_price (€/MWh)'
index_price_euro_mwh           = 'price index (€/MWh)'
index_price_min_euro_mwh       = 'price min (€/MWh)'
index_price_max_euro_mwh       = 'price max (€/MWh)'
index_price_last_euro_mwh      = 'price last (€/MWh)'
index_price_weighted_euro_mwh  = 'price weighted (€/MWh)'
index_volume_mwh               = 'index_volume (MWh)'
index_volume_non_mtf_mwh       = 'volume_non_mtf (MWh)'
index_volume_otc_mwh           = 'volume_otc (MWh)'
index_volume_trade_reg_mwh     = 'volume_trade_reg (MWh)'
index_volume_bought_mwh        = 'volume bought (MWh)'
index_volume_sold_mwh          = 'volume sold (MWh)'

### Loads
load_date_local                    = 'load_date (local)'
load_day_UTC                       = 'load_day (UTC)'
load_dt_local                      = 'load_dt (local)'
load_dt_UTC                        = 'load_dt (UTC)'
load_nature                        = 'load_nature'
load_nature_observation_mw         = 'load (MW)'
load_nature_observation_gw         = 'load (GW)'
load_nature_forecast_day1_mw       = 'load_forecast D-1 (MW)'
load_nature_forecast_day1_gw       = 'load_forecast D-1 (GW)'
load_nature_forecast_day0_mw       = 'load_forecast D-0 (MW)'
load_nature_forecast_day0_gw       = 'load_forecast D-0 (GW)'
load_nature_forecast_day1_error_mw = 'load_forecast D-1 error (MW)'
load_nature_forecast_day1_error_gw = 'load_forecast D-1 error (GW)'
load_month_UTC                     = 'load_month (UTC)'
load_time_local                    = 'load_time (local)'
load_year_UTC                      = 'load_year (UTC)'

### Maturities
maturity          = 'maturity'
maturity_day      = 'D+{nb_days}'
maturity_weekend  = 'WE+{nb_weeks}'
maturity_week     = 'W+{nb_weeks}'
maturity_month    = 'M+{nb_months}'
maturity_quarter  = 'Q+{nb_quarters}'
maturity_season   = 'S+{nb_seasons}'
maturity_gas_year = 'GY+{nb_years}'
maturity_year     = 'Y+{nb_years}'
maturity_unknown  = 'maturity_unknown'

### Options
option_type         = 'option_type'
option_call_put     = 'call_or_put'
option_strike_price = 'strike_price'

### Orders
order_actor_aggressor              = 'actor_aggressor'	
order_actor_initiator              = 'actor_initiator'	
order_begin_action                 = 'order_begin_action'
order_begin_action_insert          = 'insert'
order_begin_action_partially_dealt = 'partially_dealt'
order_begin_action_unknown         = 'unknown'
order_begin_action_update          = 'update'
order_begin_dt_local               = 'order_begin_dt (local)'
order_begin_date_UTC               = 'order_begin_date (UTC)'
order_begin_dt_UTC                 = 'order_begin_dt (UTC)'
order_counterparty_ok_bool         = 'order_counterparty_ok_bool'
order_end_action                   = 'order_end_action'
order_end_action_dealt             = 'dealt'
order_end_action_dealt_bool        = 'dealt_boolean'
order_end_action_remove            = 'remove'
order_end_action_partially_dealt   = 'partially_dealt'
order_end_action_stay              = 'stay'
order_end_action_unknown           = 'unknown'
order_end_action_update            = 'update'
order_end_dt_local                 = 'order_end_dt (local)'
order_end_dt_UTC                   = 'order_end_dt (UTC)'
order_feature_all_or_none          = 'all_or_none_boolean'
order_feature_da                   = 'order_feature_da'
order_feature_da_bloc              = 'bloc'
order_feature_da_hour              = 'hour'
order_feature_da_unknown           = 'unknown'
order_feature_hidden_power_mw      = 'hidden_power (MW)'
order_feature_sequence_span        = 'sequence_span'
order_feature_sequence_single      = 'single'
order_feature_sequence_spread      = 'spread'
order_feature_validity             = 'order_validity'
order_id                           = 'order_id'
order_id_persistent                = 'order_persistent_id'
order_id_previous                  = 'order_previous_id'
order_life_birth_dt_UTC            = 'order_life_birth_dt (UTC)'
order_life_death_dt_UTC            = 'order_life_death_dt (UTC)'
order_life_expectancy              = 'order_life_expectancy'
order_log_insert_min_dt_UTC        = 'log_insert_min_dt (UTC)'
order_log_insert_min_dt_UTC        = 'log_insert_min_dt (UTC)'
order_log_remove_max_dt_UTC        = 'log_remove_max_dt (UTC)'
order_log_update_min_dt_UTC        = 'log_update_min_dt (UTC)'
order_log_update_max_dt_UTC        = 'log_update_max_dt (UTC)'
order_market                       = 'order_market'
order_maturity                     = 'order_maturity'
order_power                        = 'order_power'
order_power_mw                     = 'order_power (MW)'
order_power_unit                   = 'order_power_unit'
order_price_euro_mwh               = 'order_price (€/MWh)'
order_rate_mw_day                  = 'order_rate (MW/day)'
order_side                         = 'order_side'
order_side_buy                     = 'buy'
order_side_sell                    = 'sell'
order_status                       = 'order_status'
order_trader_id                    = 'order_trader_id'
order_trader_name                  = 'order_trader_name'
order_volume_mwh                   = 'order_volume (MWh)'

### Outages
outage_begin_date_local               = 'outage_begin_date (local)'
outage_begin_day_UTC                  = 'outage_begin_day (UTC)'
outage_begin_dt_local                 = 'outage_begin_dt (local)'
outage_begin_dt_UTC                   = 'outage_begin_dt (UTC)'
outage_begin_month_UTC                = 'outage_begin_month (UTC)'
outage_begin_time_local               = 'outage_begin_time (local)'
outage_begin_year_UTC                 = 'outage_begin_year (UTC)'
outage_cause                          = 'outage_cause'
outage_cause_code                     = 'outage_cause_code'
outage_cause_comments                 = 'outage_cause_comments'
outage_end_date_local                 = 'outage_end_date (local)'
outage_end_dt_local                   = 'outage_end_dt (local)'
outage_end_dt_UTC                     = 'outage_end_dt (UTC)'
outage_end_time_local                 = 'outage_end_time (local)'
outage_expected_availability_mw       = 'Expected availability (MW)'
outage_expected_availability_delta_mw = '$\Delta$ expected_availability (MW)'
outage_expected_availability_gw       = 'expected_availability (GW)'
outage_remaining_power_mw             = 'outage_remaining_power (MW)'
outage_remaining_power_gw             = 'outage_remaining_power (GW)'
outage_status                         = 'outage_status'
outage_status_cancelled               = 'cancelled'
outage_status_finished                = 'finished'
outage_status_active                  = 'active'
outage_status_nan                     = 'nan'
outage_sub_begin_dt_local             = 'outage_sub_begin_dt (local)'
outage_sub_begin_dt_UTC               = 'outage_sub_begin_dt (UTC)'
outage_sub_end_dt_local               = 'outage_sub_end_dt (local)'
outage_sub_end_dt_UTC                 = 'outage_sub_end_dt (UTC)'
outage_period_begin_dt_local          = 'outage_period_begin_dt (local)'
outage_period_begin_dt_UTC            = 'outage_period_begin_dt (UTC)'
outage_period_end_dt_local            = 'outage_period_end_dt (local)'
outage_period_end_dt_UTC              = 'outage_period_end_dt (UTC)'
outage_type                           = 'outage_type'
outage_type_fortuitous                = 'fortuitous'
outage_type_planned                   = 'planned'

### Portfolios
portfolio_id = 'portfolio_id'

### Positions
position_mw       = 'position (MW)'
position_delta_mw = '$\Delta$ position (MW)'

### Producers
producer_id           = 'producer_id'
producer_name         = 'producer_name'
producer_name_alpiq   = 'Alpiq'
producer_name_edf     = 'EDF'
producer_name_engie   = 'ENGIE'
producer_name_eon     = 'EON'
producer_name_gazel   = 'Gazel'
producer_name_info    = 'producer_name_info'
producer_name_pss     = 'PSS'
producer_name_total   = 'Total'
producer_name_unknown = 'producer_unknown'

### Production
production_date_local                  = 'production_date (local)'
production_date_UTC                    = 'production_date (UTC)'
production_day_UTC                     = 'production_day (UTC)'
production_dt_tz                       = 'production_dt ({tz})'
production_dt_local                    = 'production_dt (local)'
production_dt_UTC                      = 'production_dt (UTC)'
production_month_UTC                   = 'production_month (UTC)'
production_nature                      = 'production_nature'
production_nature_observation_mw       = 'production (MW)'
production_nature_observation_gw       = 'production (GW)'
production_negative_part_mw            = 'production positive part (MW)'
production_positive_part_mw            = 'production negative part (MW)'
production_power_mw                    = 'production_power (MW)'
production_source                      = 'production_source'
production_source_biomass              = 'biomass'
production_source_fossil_coal          = 'fossil_coal'
production_source_fossil_gas           = 'fossil_gas'
production_source_fossil_oil           = 'fossil_oil'
production_source_hydro_pumped_storage = 'hydro_pumped_storage'
production_source_hydro_reservoir      = 'hydro_reservoir'
production_source_hydro_run_of_river   = 'hydro_run_of_river'
production_source_marine               = 'marine'
production_source_nuclear              = 'nuclear'
production_source_solar                = 'solar'
production_source_other                = 'other'
production_source_unknown              = 'unknown'
production_source_wind_offshore        = 'wind_offshore'
production_source_wind_onshore         = 'wind_onshore'
production_step_dt_local               = 'production_step_dt (local)'
production_step_dt_UTC                 = 'production_step_dt (UTC)'
production_time_local                  = 'production_time (local)'
production_time_UTC                    = 'production_time (UTC)'
production_volume_mwh                  = 'production_volume (MWh)'
production_year_UTC                    = 'production_year (UTC)'

### Publications
publication_creation_dt_local = 'creation_dt (local)'
publication_creation_dt_UTC   = 'creation_dt (UTC)'
publication_day_local         = 'publication_day (local)'
publication_day_UTC           = 'publication_day (UTC)'
publication_dt_local          = 'publication_dt (local)'
publication_dt_UTC            = 'publication_dt (UTC)'
publication_id                = 'publication_id'
publication_month_local       = 'publication_month (local)'
publication_month_UTC         = 'publication_month (UTC)'
publication_year_local        = 'publication_year (local)'
publication_year_UTC          = 'publication_year (UTC)'
publication_version           = 'version'

### Quantity
quantity_value   = 'quantity_value'
quantity_unit    = 'quantity_unit'
quantity_unit_gw = '(GW)'
quantity_unit_mw = '(MW)'

### Time
time_date_UTC            = 'time_date (UTC)'
time_dt_tz               = 'dt ({tz})'
time_dt_local            = 'dt (local)'
time_dt_UTC              = 'dt (UTC)'
time_hour_UTC            = 'hour (UTC)'
time_hours_covered_nb    = 'nb_covered_hours'
time_hours_covered_ratio = 'ratio_covered_hours'
time_nb_hours            = 'nb_hours'
time_nb_days             = 'nb_days'
time_resolution_code     = 'resolution_code'
time_zone                = 'time_zone'

### Trades
trade_actor_aggressor               = 'trade_actor_aggressor'
trade_actor_aggressor_true          = 1
trade_actor_aggressor_false         = 0
trade_actor_aggressor_unknown       = -1
trade_actor_initiator               = 'trade_actor_initiator'
trade_actor_initiator_true          = 1
trade_actor_initiator_false         = 0
trade_actor_initiator_unknown       = -1
trade_actor_leg                     = 'trade_actor_leg'
trade_actor_leg_buy                 = +1
trade_actor_leg_sell                = -1
trade_actor_role                    = 'trade_actor_role'
trade_actor_role_aggressor          = 'aggressor'
trade_actor_role_initiator          = 'initiator'
trade_actor_role_bilateral          = 'bilateral'
trade_actor_role_unknown            = 'unknown'
trade_actor_role                    = 'trade_actor_role'
trade_aggressor                     = 'trade_aggressor'
trade_aggressor_info                = 'trade_aggressor_info'
trade_buyer                         = 'trade_buyer'
trade_buyer_portfolio               = 'trade_buyer_portfolio'
trade_buyer_country                 = 'trade_buyer_country'
trade_buyer_info                    = 'trade_buyer_info'
trade_cashflow_euro                 = 'trade_cashflow (€)'
trade_counterparty                  = 'trade_counterparty'
trade_counterparty_info             = 'trade_counterparty_info'
trade_counterparty_ok_bool          = 'trade_counterparty_ok_bool'
trade_date_local                    = 'trade_date (local)'
trade_dt_local                      = 'trade_dt (local)'
trade_dt_UTC                        = 'trade_dt (UTC)'
trade_dt_UK                         = 'trade_dt (UK)'
trade_hour_UK                       = 'trade_time (UK)'
trade_id                            = 'trade_id'
trade_initiator                     = 'trade_initiator'
trade_initiator_info                = 'trade_initiator_info'
trade_intermediary                  = 'trade_intermediary'
trade_market                        = 'trade_market'
trade_market_type                   = 'trade_market_type'
trade_maturity                      = 'trade_maturity'
trade_outage_alert                  = 'trade_outage_alert'
trade_outage_time_delta             = 'trade_outage_time_delta'
trade_power                         = 'trade_power'
trade_power_mw                      = 'trade_power (MW)' # Trades power are multiples of contracts powers
trade_power_mwh_day                 = 'trade_power (MWh/day)' # Trades power are multiples of contracts powers
trade_power_gw                      = 'trade_power (GW)'
trade_power_signed_mw               = 'trade_power_signed (MW)'
trade_power_unit                    = 'trade_power_unit'
trade_price_euro_mwh                = 'trade_price (€/MWh)'
trade_pricing                       = 'trade_pricing'
trade_seller                        = 'trade_seller'
trade_seller_portfolio              = 'trade_seller_portfolio'
trade_seller_country                = 'trade_seller_country'
trade_seller_info                   = 'trade_seller_info'
trade_suspicion_level               = 'trade_volume_suspect (MW.MW.h)'
trade_time_local                    = 'trade_time (local)'
trade_time_UTC                      = 'trade_time (UTC)'
trade_trader_id                     = 'trader_id'
trade_trader_name                   = 'trader_name'
trade_valuation_next_dt_UTC         = 'trade_valuation_next_dt_UTC'
trade_valuation_next_price_euro_mwh = 'trade_valuation_next_price_euro_mwh'
trade_valuation_prev_dt_UTC         = 'trade_valuation_prev_dt_UTC'
trade_valuation_prev_price_euro_mw  = 'trade_valuation_prev_price_euro_mw'
trade_volume_mwh                    = 'trade_volume (MWh)' # Trades volumes are multiples of contracts volumes
trade_volume_gwh                    = 'trade_volume (GWh)'
trade_volume_signed_mwh             = 'trade_volume_signed (MWh)'
trade_wh_local                      = 'trade_wh (local)'

### Units Production
unit_eic                = 'unit_eic'
unit_name               = 'unit_name'
unit_nameplate_capacity = 'nameplate_capacity'
unit_type               = 'unit_type'
unit_type_plant         = "plant"
unit_type_group         = "group"
unit_voltage_connection = 'unit_voltage_connection'

### Weather
weather_dt_UTC              = 'weather_dt (UTC)'
weather_nature              = 'weather_nature'
weather_nature_forecast     = 'forecast'
weather_nature_observation  = 'observation'
weather_nebulosity          = 'nebulosity (%)'
weather_physical_quantity   = 'physical_quantity'
weather_site_id             = 'weather_site_id'
weather_site_name           = 'weather_site_name'
weather_temperature_celsius = 'temperature (°C)'
weather_temperature_kelvin  = 'temperature (K)'
weather_wind_speed          = 'wind_speed (m/s)'




