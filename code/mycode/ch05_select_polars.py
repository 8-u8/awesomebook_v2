#%% install libraries
import pathlib
import polars as pl

#%% load data
datadir = pathlib.Path.cwd().parent / 'data'

pl_hotel = pl.read_parquet(datadir / 'hotel.parquet')
pl_customer = pl.read_parquet(datadir / "customer.parquet")
pl_reservation = pl.read_parquet(datadir / "reservation.parquet")

# %%
pl_reservation.select(
    pl.col(
        [
        "reservation_id",
        "hotel_id",
        "customer_id",
        "checkin_date",
        "checkout_date",
        ] # このあたりはなんとかなりそう。
    )
)

# %%
