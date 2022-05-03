from typing import *

from faker.providers import BaseProvider

from .models.enum import EMapTag
from .models import MapDetailMetadata, MapStats, UserDetail, EAccountType, UserStats, UserDiffStats, MapVersion, EMapState, \
    MapDifficulty, ECharacteristic, EDifficulty, MapParitySummary
from .models import MapDetail


class BeatSaverProvider(BaseProvider):
    def _value_or_none(self, value: any) -> Optional[any]:
        if self.random_int(0, 1) == 0:
            return None

        return value

    def beatmap_key(self) -> str:
        max_key = "1b501"
        return hex(self.random_int(1, int(max_key, 16)))[2:]

    def beatmap_hash(self) -> str:
        return self.generator.sha1(raw_output=False)

    def map_details_by_hash(self, beatmap_hashes: List[str] = None):
        map_details = []

        for beatmap_hash in beatmap_hashes:
            map_details.append(self.map_detail(beatmap_hash=beatmap_hash))

        return map_details

    def map_details(self, amount: int = None, *args, **kwargs) -> List[MapDetail]:
        map_details = []

        for _ in range(amount if amount is not None else self.random_int(0, 10)):
            map_details.append(self.map_detail(*args, **kwargs))

        return map_details

    def map_detail(self, beatmap_key: str = None, beatmap_hash: str = None, uploader_id: int = None) -> MapDetail:
        if beatmap_key is None:
            beatmap_key = self.beatmap_key()

        map_detail = MapDetail()

        map_detail.id = beatmap_key
        map_detail.name = self.generator.text(max_nb_chars=30)
        map_detail.description = self.generator.sentence()
        map_detail.uploader = self.user_detail(user_id=uploader_id)
        map_detail.metadata = self.map_detail_metadata()
        map_detail.stats = self.map_stats()
        map_detail.automapper = self.generator.pybool()
        map_detail.ranked = self.generator.pybool()
        map_detail.qualified = self.generator.pybool()
        map_detail.versions = self.map_versions(beatmap_key, beatmap_hash)
        map_detail.curator = self._value_or_none(self.generator.user_name())
        map_detail.tags = self._value_or_none(self.random_choices(list(EMapTag), 5))
        map_detail.created_at = self.generator.past_datetime()
        map_detail.curated_at = self._value_or_none(self.generator.past_datetime())
        map_detail.updated_at = self.generator.past_datetime()
        map_detail.deleted_at = self._value_or_none(self.generator.past_datetime())
        map_detail.uploaded = self._value_or_none(self.generator.past_datetime())
        map_detail.last_published_at = self._value_or_none(self.generator.past_datetime())

        return map_detail

    def map_detail_metadata(self) -> MapDetailMetadata:
        map_detail_metadata = MapDetailMetadata()

        map_detail_metadata.bpm = float(self.numerify("%##.###"))
        map_detail_metadata.duration = self.random_int(100, 999)
        map_detail_metadata.level_author_name = self.generator.user_name()
        map_detail_metadata.song_author_name = self.generator.user_name()
        map_detail_metadata.song_name = self.generator.text(max_nb_chars=30)
        map_detail_metadata.song_sub_name = self.generator.text(max_nb_chars=30)

        return map_detail_metadata

    def map_stats(self) -> MapStats:
        map_stats = MapStats()

        map_stats.downloads = self.random_int(0, 99999)
        map_stats.downvotes = self.random_int(0, 99999)
        map_stats.upvotes = self.random_int(0, 99999)
        map_stats.plays = self.random_int(0, 999999)
        # Not sure how this is calculated at beat saver
        map_stats.score = abs(map_stats.upvotes / (map_stats.upvotes + map_stats.downvotes))

        return map_stats

    def user_detail(self, user_id: int = None, username: str = None) -> UserDetail:
        user_detail = UserDetail()

        user_detail.id = user_id if user_id is not None else self.random_int(1, 99999999)
        user_detail.name = username if username is not None else self.generator.user_name()
        user_detail.unique_set = self.generator.pybool()
        user_detail.hash = self._value_or_none(self.generator.sha1(raw_output=False))
        user_detail.testplay = self._value_or_none(self.generator.pybool())
        user_detail.avatar = self.generator.image_url(80, 80)
        user_detail.stats = self._value_or_none(self.user_stats())
        user_detail.type = self.random_choices(list(EAccountType), 1)

        return user_detail

    def user_stats(self) -> UserStats:
        user_stats = UserStats()

        user_stats.total_upvotes = self.random_int(0, 99999999)
        user_stats.total_downvotes = self.random_int(0, 99999999)
        user_stats.total_maps = self.random_int(0, 99999999)
        user_stats.ranked_maps = self.random_int(0, 99999999)
        user_stats.avg_bpm = float(self.random_int(0, 99999999))
        user_stats.avg_score = float(self.random_int(0, 99999999))
        user_stats.avg_duration = float(self.random_int(0, 99999999))
        user_stats.first_upload = self._value_or_none(self.generator.past_datetime())
        user_stats.last_upload = self._value_or_none(self.generator.past_datetime())
        user_stats.diff_stats = self._value_or_none(self.user_diff_stats())

        return user_stats

    def user_diff_stats(self) -> UserDiffStats:
        user_diff_stats = UserDiffStats()

        user_diff_stats.easy = self.random_int(0, 99999)
        user_diff_stats.normal = self.random_int(0, 99999)
        user_diff_stats.hard = self.random_int(0, 99999)
        user_diff_stats.expert = self.random_int(0, 99999)
        user_diff_stats.expert_plus = self.random_int(0, 99999)

        user_diff_stats.total = user_diff_stats.easy \
                                + user_diff_stats.normal \
                                + user_diff_stats.hard \
                                + user_diff_stats.expert \
                                + user_diff_stats.expert_plus

        return user_diff_stats

    def map_versions(self, beatmap_key: str = None, beatmap_hash: str = None, amount: int = None) -> List[MapVersion]:
        map_versions = []

        for index in range(amount if amount is not None else self.random_int(1, 10)):
            map_versions.append(self.map_version(beatmap_key, beatmap_hash))

        return map_versions

    def map_version(self, beatmap_key: str = None, beatmap_hash: str = None) -> MapVersion:
        if beatmap_key is None:
            beatmap_key = self.beatmap_key()

        if beatmap_hash is None:
            beatmap_hash = self.beatmap_hash()

        map_version = MapVersion()

        map_version.hash = beatmap_hash
        map_version.key = self._value_or_none(beatmap_key)
        map_version.state = self.random_choices(list(EMapState), 1)[0]
        map_version.created_at = self.generator.past_datetime()
        map_version.sage_score = self._value_or_none(self.random_int(-10, 10))
        map_version.diffs = self.map_difficulties()
        map_version.feedback = self._value_or_none(self.generator.sentence())
        map_version.testplay_at = self._value_or_none(self.generator.past_datetime())
        map_version.testplays = self._value_or_none(None)
        map_version.download_url = self.generator.uri()
        map_version.cover_url = self.generator.image_url(256, 265)
        map_version.preview_url = self.generator.uri()
        map_version.scheduled_at = self._value_or_none(self.generator.date_time_this_year())

        return map_version

    def map_difficulties(self, amount: int = None) -> List[MapDifficulty]:
        map_diffs = []

        for index in range(amount if amount is not None else self.random_int(0, 10)):
            map_diffs.append(self.map_difficulty())

        return map_diffs

    def map_difficulty(self) -> MapDifficulty:
        map_difficulty = MapDifficulty()

        map_difficulty.njs = float(self.numerify("%##.###"))
        map_difficulty.offset = float(self.numerify("%##.###"))
        map_difficulty.notes = self.random_int(0, 9999)
        map_difficulty.bombs = self.random_int(0, 9999)
        map_difficulty.obstacles = self.random_int(0, 9999)
        map_difficulty.nps = float(self.numerify("%##.###"))
        map_difficulty.length = float(self.numerify("%##.###"))
        map_difficulty.characteristic = self.random_choices(list(ECharacteristic), 1)
        map_difficulty.difficulty = self.random_choices(list(EDifficulty), 1)
        map_difficulty.events = self.random_int(0, 9999)
        map_difficulty.chroma = self.generator.pybool()
        map_difficulty.me = self.generator.pybool()
        map_difficulty.ne = self.generator.pybool()
        map_difficulty.cinema = self.generator.pybool()
        map_difficulty.seconds = float(self.numerify("%##.###"))
        map_difficulty.parity_summary = self.map_parity_summary()
        map_difficulty.stars = self._value_or_none(float(self.numerify("%##.###")))

        return map_difficulty

    def map_parity_summary(self) -> MapParitySummary:
        map_parity_summary = MapParitySummary()

        map_parity_summary.errors = self.random_int(0, 999)
        map_parity_summary.resets = self.random_int(0, 999)
        map_parity_summary.warns = self.random_int(0, 999)

        return map_parity_summary
