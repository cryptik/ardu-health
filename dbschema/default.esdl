module default {

    type Drone {
        required property name -> str;
        required property aircraft_id -> str;
        property callsign -> str;
        property firmware -> str;
    }

    type Flight_Test {
        required property tag -> str;
        property data -> array<str>;
    }

}   
