"""HomeBot Android library."""

class _AndroidVersion:
	def __init__(self,
	             version_code: str,
	             version_name: str,
	             api_version: int,
	            ):
		self.version_code = version_code
		self.version_name = version_name
		self.api_version = api_version

		self.version_short = self.__version_short()

	def __version_short(self):
		version_name_split = self.version_name.split()
		version_short = version_name_split[0][0]

		return version_short

class AndroidVersion(_AndroidVersion):
	BASE = _AndroidVersion("1.0", "1.0", 1)
	BASE_1_1 = _AndroidVersion("1.1", "1.1", 2)
	CUPCAKE = _AndroidVersion("1.5", "Cupcake", 3)
	DONUT = _AndroidVersion("1.6", "Donut", 4)
	ECLAIR = _AndroidVersion("2.0", "Eclair", 5)
	ECLAIR_0_1 = _AndroidVersion("2.0.1", "Eclair incremental update", 6)
	ECLAIR_MR1 = _AndroidVersion("2.1", "Eclair MR1", 7)
	FROYO = _AndroidVersion("2.2", "Froyo", 8)
	GINGERBREAD = _AndroidVersion("2.3", "Gingerbread", 9)
	GINGERBREAD_MR1 = _AndroidVersion("2.3.3", "Gingerbread MR1", 10)
	HONEYCOMB = _AndroidVersion("3.0", "Honeycomb", 11)
	HONEYCOMB_MR1 = _AndroidVersion("3.1", "Honeycomb MR1", 12)
	HONEYCOMB_MR2 = _AndroidVersion("3.2", "Honeycomb MR2", 13)
	ICE_CREAM_SANDWICH = _AndroidVersion("4.0", "Ice Cream Sandwich", 14)
	ICE_CREAM_SANDWICH_MR1 = _AndroidVersion("4.0.3", "Ice Cream Sandwich MR1", 15)
	JELLY_BEAN = _AndroidVersion("4.1", "Jelly Bean", 16)
	JELLY_BEAN_MR1 = _AndroidVersion("4.2", "Jelly Bean MR1", 17)
	JELLY_BEAN_MR2 = _AndroidVersion("4.3", "Jelly Bean MR2", 18)
	KITKAT = _AndroidVersion("4.4", "KitKat", 19)
	KITKAT_WATCH = _AndroidVersion("4.4W", "KitKat Watch", 20)
	LOLLIPOP = _AndroidVersion("5.0", "Lollipop", 21)
	LOLLIPOP_MR1 = _AndroidVersion("5.1", "Lollipop MR1", 22)
	M = _AndroidVersion("6.0", "Marshmallow", 23)
	N = _AndroidVersion("7.0", "Nougat", 24)
	N_MR1 = _AndroidVersion("7.1", "Nougat MR1", 25)
	O = _AndroidVersion("8.0", "Oreo", 26)
	O_MR1 = _AndroidVersion("8.1", "Oreo MR1", 27)
	P = _AndroidVersion("9", "Pie", 28)
	Q = _AndroidVersion("10", "Q", 29)
	R = _AndroidVersion("11", "R", 30)
	S = _AndroidVersion("12", "S", 31)

	_ALL = [
		BASE,
		BASE_1_1,
		CUPCAKE,
		DONUT,
		ECLAIR,
		ECLAIR_0_1,
		ECLAIR_MR1,
		FROYO,
		GINGERBREAD,
		GINGERBREAD_MR1,
		HONEYCOMB,
		HONEYCOMB_MR1,
		HONEYCOMB_MR2,
		ICE_CREAM_SANDWICH,
		ICE_CREAM_SANDWICH_MR1,
		JELLY_BEAN,
		JELLY_BEAN_MR1,
		JELLY_BEAN_MR2,
		KITKAT,
		KITKAT_WATCH,
		LOLLIPOP,
		LOLLIPOP_MR1,
		M,
		N,
		N_MR1,
		O,
		O_MR1,
		P,
		Q,
		R,
		S,
	]

	@staticmethod
	def from_version_code(version_code: str):
		for version in AndroidVersion._ALL:
			if version.version_code == version_code:
				return version
		return None

	@staticmethod
	def from_version_name(version_name: str):
		for version in AndroidVersion._ALL:
			if version.version_name == version_name:
				return version
		return None

	@staticmethod
	def from_api_version(api_version: int):
		for version in AndroidVersion._ALL:
			if version.api_version == api_version:
				return version
		return None

	@staticmethod
	def from_version_short(version_short: str):
		for version in AndroidVersion._ALL:
			if version.version_short == version_short:
				return version
		return None
