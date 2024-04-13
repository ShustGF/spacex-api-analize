"""Файл с функциями для работы с API SpaceX"""

import requests
from entities import Capsules, Cores, Crew, LaunchesSpaceX, StarlinkSat   


def get_data_from_url(url: str):
    """Функция загрузки данных по URL"""
    req_answer = requests.get(url, timeout=30)
    if req_answer.status_code == 404:
        raise AttributeError("Неверное значение URL-адреса")
    return req_answer.text


def get_starlinks(sat_json):
    """Функция для работы с данными спутников Starlink"""
    starlink_sat = StarlinkSat(
        spacetrack=sat_json["spaceTrack"],
        version=sat_json["version"],
        launch=sat_json["launch"],
        longitude=sat_json["longitude"],
        latitude=sat_json["latitude"],
        height_km=sat_json["height_km"],
        velocity_kms=sat_json["velocity_kms"],
        id=sat_json["id"],
    )
    return starlink_sat


def get_launches(sat_json):
    """Функция для работы с данными запусков SpaceX"""
    launches = LaunchesSpaceX(
        fairings=sat_json["fairings"],
        links=sat_json["links"],
        static_fire_date_utc=sat_json["static_fire_date_utc"],
        static_fire_date_unix=sat_json["static_fire_date_unix"],
        tbd=sat_json["tbd"],
        net=sat_json["net"],
        window=sat_json["window"],
        rocket=sat_json["rocket"],
        success=sat_json["success"],
        failures=sat_json["failures"],
        details=sat_json["details"],
        crew=sat_json["crew"],
        ships=sat_json["ships"],
        capsules=sat_json["capsules"],
        payloads=sat_json["payloads"],
        launchpad=sat_json["launchpad"],
        auto_update=sat_json["auto_update"],
        flight_number=sat_json["flight_number"],
        name=sat_json["name"],
        date_utc=sat_json["date_utc"],
        date_unix=sat_json["date_unix"],
        date_local=sat_json["date_local"],
        date_precision=sat_json["date_precision"],
        upcoming=sat_json["upcoming"],
        cores=sat_json["cores"],
        id=sat_json["id"],
    )
    return launches


def get_capsules(sat_json):
    """Функция для работы с данными запусков SpaceX"""
    capsules = Capsules(
        reuse_count=sat_json["reuse_count"],
        water_landings=sat_json["water_landings"],
        land_landings=sat_json["land_landings"],
        last_update=sat_json["last_update"],
        launches=sat_json["launches"],
        serial=sat_json["serial"],
        status=sat_json["status"],
        type=sat_json["type"],
        id=sat_json["id"],
    )
    return capsules


def get_cores(sat_json):
    """Функция получения данных об объекстах SpaceX вернувшихся на землю"""
    cores = Cores(
        block=sat_json["block"],
        reuse_count=sat_json["reuse_count"],
        rtls_attempts=sat_json["rtls_attempts"],
        rtls_landings=sat_json["rtls_landings"],
        asds_attempts=sat_json["asds_attempts"],
        asds_landings=sat_json["asds_landings"],
        last_update=sat_json["last_update"],
        launches=sat_json["launches"],
        serial=sat_json["serial"],
        status=sat_json["status"],
        id=sat_json["id"],
    )
    return cores


def get_crew(sat_json):
    """Функция получения данных о носителях Crew"""
    crew = Crew(
        name=sat_json["name"],
        agency=sat_json["agency"],
        image=sat_json["image"],
        wikipedia=sat_json["wikipedia"],
        launches=sat_json["launches"],
        status=sat_json["status"],
        id=sat_json["id"],
    )
    return crew
