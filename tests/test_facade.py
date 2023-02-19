from concurrent.futures import Future

from aiohttp import ClientSession

from data.data import Data
from modules.facade import CurrentValues
from modules.manager import Manager
from tests.prerequisites import Start

Start()

def test_default_values():
    mng = Manager()
    assert CurrentValues.download_dir == Data.DefaultValues.download_dir
    assert CurrentValues.genre == Data.DefaultValues.genre
    assert CurrentValues.form == Data.DefaultValues.form
    assert CurrentValues.is_lossless == Data.DefaultValues.is_lossless
    assert CurrentValues.quantity == Data.DefaultValues.quantity
    assert CurrentValues.is_period == Data.DefaultValues.is_period
    assert CurrentValues.threads == Data.DefaultValues.threads
    assert CurrentValues.is_rewrite_files == Data.DefaultValues.is_rewrite_files
    assert CurrentValues.is_file_history == Data.DefaultValues.is_file_history

    assert mng._downloading is None
    assert CurrentValues.session is None

    assert mng.progress[int]
    assert mng.success[int]
    assert mng.search[int, int]
    assert mng.message[str]
    assert mng.file_info[int, int]

    assert CurrentValues.total_files == 0
    assert CurrentValues.total_downloaded_files == 0
    assert CurrentValues.total_downloaded == 0
    assert CurrentValues.total_size == 0

def test_default_types():
    mng = Manager()
    assert isinstance(CurrentValues.download_dir, str)
    assert isinstance(CurrentValues.genre, str)
    assert isinstance(CurrentValues.form, str)
    assert isinstance(CurrentValues.is_lossless, bool)
    assert isinstance(CurrentValues.quantity, int)
    assert isinstance(CurrentValues.is_period, bool)
    assert isinstance(CurrentValues.threads, int)
    assert isinstance(CurrentValues.is_rewrite_files, bool)
    assert isinstance(CurrentValues.is_file_history, bool)

    assert isinstance(mng._downloading, Future | None)
    assert isinstance(CurrentValues.session, ClientSession | None)

    assert isinstance(CurrentValues.total_files, int)
    assert isinstance(CurrentValues.total_downloaded_files, int)
    assert isinstance(CurrentValues.total_downloaded, int)
    assert isinstance(CurrentValues.total_size, int)
