from enum import Enum

class SongCodec(Enum):
  AAC_LEGACY = "aac-legacy"
  AAC_HE_LEGACY = "aac-he-legacy"
  AAC = "aac"
  AAC_HE = "aac-he"
  AAC_BINAURAL = "aac-binaural"
  AAC_DOWNMIX = "aac-downmix"
  AAC_HE_BINAURAL = "aac-he-binaural"
  AAC_HE_DOWNMIX = "aac-he-downmix"
  ATMOS = "atmos"
  AC3 = "ac3"
  ALAC = "alac"