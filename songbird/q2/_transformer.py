import qiime2

from q2_dada2 import SongbirdStatsFormat
from q2_dada2.plugin_setup import plugin


@plugin.register_transformer
def _1(ff: SongbirdStatsFormat) -> qiime2.Metadata:
    return qiime2.Metadata.load(str(ff))


@plugin.register_transformer
def _2(obj: qiime2.Metadata) -> SongbirdStatsFormat:
    ff = SongbirdStatsFormat()
    obj.save(str(ff))
    return ff