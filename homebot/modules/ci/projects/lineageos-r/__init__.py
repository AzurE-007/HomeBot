"""LineageOS R CI project."""

from homebot.modules.ci.projects.aosp.project import AOSPProject

class Project(AOSPProject):
	name = "LineageOS"
	version = "18.1"
	android_version = "11"
	category = "ROMs"
	lunch_prefix = "lineage"
	lunch_suffix = "userdebug"
	build_target = "bacon"
	artifacts = "lineage-*.zip"
