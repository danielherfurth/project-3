CREATE TABLE sqlite_master (
                           type text,
                           name text,
                           tbl_name text,
                           rootpage int,
                           sql text
                           );

INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'iats', 'iats', 37578, 'CREATE TABLE "iats" (
                         frame integer,
                         time_ms integer,
                         rpm integer,
                         vss real,
                         gear integer,
                         map real,
                         bp real,
                         bp_cmd real,
                         tpedal integer,
                         tplate integer,
                         airc integer,
                         iat real,
                         iat2 real,
                         ect real,
                         ect2 real,
                         pa real,
                         difp real,
                         difpcmd real,
                         wg real,
                         wgcmd real,
                         purge integer,
                         bc_duty integer,
                         af real,
                         af_bank_2 integer,
                         af_corr real,
                         afcmd real,
                         afcmd_bank_2 integer,
                         s_trim integer,
                         trim integer,
                         k_level integer,
                         k_retard integer,
                         k_retard_1 integer,
                         k_retard_2 integer,
                         k_retard_3 integer,
                         k_retard_4 integer,
                         k_control integer,
                         k_count integer,
                         k_count_1 integer,
                         k_count_2 integer,
                         k_count_3 integer,
                         k_count_4 integer,
                         bat real,
                         abs_lf real,
                         abs_rf real,
                         abs_lr real,
                         abs_rr real,
                         brake_press real,
                         steer_ang integer,
                         g_lat real,
                         g_long real,
                         yaw real,
                         tc_v integer,
                         tc_ecuslip integer,
                         tc_r integer,
                         tc_lf integer,
                         tc_rf integer,
                         tc_lr integer,
                         tc_rr integer,
                         tc_slip integer,
                         tc_turn integer,
                         tc_overslip integer,
                         tc_out integer
                         )');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'iats2', 'iats2', 362, 'CREATE TABLE "iats2"
(
    frame     INTEGER,
    time_ms   INTEGER,
    rpm       INTEGER,
    vss       REAL,
    gear      INTEGER,
    map       REAL,
    bp        REAL,
    tpedal    INTEGER,
    iat       REAL,
    iat2      REAL,
    af        REAL,
    steer_ang INTEGER,
    g_lat     REAL,
    g_long    REAL
)');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'gfb', 'gfb', 365, 'CREATE TABLE "gfb" (
                        frame integer,
                        time_ms integer,
                        time_us integer,
                        rpm integer,
                        vss real,
                        gear integer,
                        ptank integer,
                        map real,
                        bp real,
                        bp_cmd real,
                        tpedal integer,
                        tplate integer,
                        afm_v real,
                        afm_hz integer,
                        afm real,
                        afm_c integer,
                        airc integer,
                        egr integer,
                        iat real,
                        iat2 real,
                        ect real,
                        ect2 real,
                        pa real,
                        oil_press real,
                        cvt_temp integer,
                        inj real,
                        inj_bank_2 integer,
                        duty integer,
                        difp real,
                        difpcmd real,
                        fuelp integer,
                        ign integer,
                        cam integer,
                        camcmd integer,
                        excam integer,
                        excamcmd integer,
                        wg real,
                        wgcmd real,
                        vts text,
                        svs text,
                        purge integer,
                        accl text,
                        bc_duty integer,
                        af real,
                        af_bank_2 integer,
                        af_corr real,
                        wide_v integer,
                        wide integer,
                        afcmd real,
                        afcmd_bank_2 integer,
                        s_trim integer,
                        l_trim integer,
                        s_trim_bank_2 integer,
                        l_trim_bank_2 integer,
                        trim integer,
                        fuel_status integer,
                        fuel_status_bank_2 integer,
                        ethanol integer,
                        k_level integer,
                        k_retard integer,
                        k_retard_1 integer,
                        k_retard_2 integer,
                        k_retard_3 integer,
                        k_retard_4 integer,
                        k_control integer,
                        ign_limit integer,
                        k_count integer,
                        k_count_1 integer,
                        k_count_2 integer,
                        k_count_3 integer,
                        k_count_4 integer,
                        k_count_5 integer,
                        k_count_6 integer,
                        bat real,
                        cat_t real,
                        abs_lf real,
                        abs_rf real,
                        abs_lr real,
                        abs_rr real,
                        clutch_pos integer,
                        brake_press real,
                        steer_ang integer,
                        steer_trq integer,
                        g_lat real,
                        g_long real,
                        g_z integer,
                        yaw real,
                        eco integer,
                        fuel_used integer,
                        tc_v integer,
                        tc_ecuslip integer,
                        tc_r integer,
                        tc_lf integer,
                        tc_rf integer,
                        tc_lr integer,
                        tc_rr integer,
                        tc_slip integer,
                        tc_turn integer,
                        tc_overslip integer,
                        tc_out integer
                        )');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'long_term', 'long_term', 2, 'CREATE TABLE "long_term" (
                              frame integer,
                              time_ms integer,
                              time_us integer,
                              rpm integer,
                              vss real,
                              gear integer,
                              ptank integer,
                              map real,
                              bp real,
                              bp_cmd real,
                              tpedal integer,
                              tplate integer,
                              afm_v real,
                              afm_hz integer,
                              afm real,
                              afm_c integer,
                              airc integer,
                              egr integer,
                              iat real,
                              iat2 real,
                              ect real,
                              ect2 real,
                              pa real,
                              oil_press real,
                              cvt_temp integer,
                              inj real,
                              inj_bank_2 integer,
                              duty integer,
                              difp real,
                              difpcmd real,
                              fuelp integer,
                              ign integer,
                              cam integer,
                              camcmd integer,
                              excam integer,
                              excamcmd integer,
                              wg real,
                              wgcmd real,
                              vts text,
                              svs text,
                              purge integer,
                              accl text,
                              bc_duty integer,
                              af real,
                              af_bank_2 integer,
                              af_corr real,
                              wide_v integer,
                              wide integer,
                              afcmd real,
                              afcmd_bank_2 integer,
                              s_trim integer,
                              l_trim integer,
                              s_trim_bank_2 integer,
                              l_trim_bank_2 integer,
                              trim integer,
                              fuel_status integer,
                              fuel_status_bank_2 integer,
                              ethanol integer,
                              k_level integer,
                              k_retard integer,
                              k_retard_1 integer,
                              k_retard_2 integer,
                              k_retard_3 integer,
                              k_retard_4 integer,
                              k_control integer,
                              ign_limit integer,
                              k_count integer,
                              k_count_1 integer,
                              k_count_2 integer,
                              k_count_3 integer,
                              k_count_4 integer,
                              k_count_5 integer,
                              k_count_6 integer,
                              bat real,
                              cat_t real,
                              abs_lf real,
                              abs_rf real,
                              abs_lr real,
                              abs_rr real,
                              clutch_pos integer,
                              brake_press real,
                              steer_ang integer,
                              steer_trq integer,
                              g_lat real,
                              g_long real,
                              g_z integer,
                              yaw real,
                              eco integer,
                              fuel_used integer,
                              tc_v integer,
                              tc_ecuslip integer,
                              tc_r integer,
                              tc_lf integer,
                              tc_rf integer,
                              tc_lr integer,
                              tc_rr integer,
                              tc_slip integer,
                              tc_turn integer,
                              tc_overslip integer,
                              tc_out integer
                              )');
INSERT INTO sqlite_master (type, name, tbl_name, rootpage, sql) VALUES ('table', 'tc_disp', 'tc_disp', 500, 'CREATE TABLE "tc_disp" (
                            frame integer,
                            time_ms integer,
                            time_us integer,
                            rpm integer,
                            vss real,
                            gear integer,
                            ptank integer,
                            map real,
                            bp real,
                            bp_cmd real,
                            tpedal integer,
                            tplate integer,
                            afm_v real,
                            afm_hz integer,
                            afm real,
                            afm_c integer,
                            airc integer,
                            egr integer,
                            iat real,
                            iat2 real,
                            ect real,
                            ect2 real,
                            pa real,
                            oil_press real,
                            cvt_temp integer,
                            inj real,
                            inj_bank_2 integer,
                            duty integer,
                            difp real,
                            difpcmd real,
                            fuelp integer,
                            ign integer,
                            cam integer,
                            camcmd integer,
                            excam integer,
                            excamcmd integer,
                            wg real,
                            wgcmd real,
                            vts text,
                            svs text,
                            purge integer,
                            accl text,
                            bc_duty integer,
                            af real,
                            af_bank_2 integer,
                            af_corr real,
                            wide_v integer,
                            wide integer,
                            afcmd real,
                            afcmd_bank_2 integer,
                            s_trim integer,
                            l_trim integer,
                            s_trim_bank_2 integer,
                            l_trim_bank_2 integer,
                            trim integer,
                            fuel_status integer,
                            fuel_status_bank_2 integer,
                            ethanol integer,
                            k_level integer,
                            k_retard integer,
                            k_retard_1 integer,
                            k_retard_2 integer,
                            k_retard_3 integer,
                            k_retard_4 integer,
                            k_control integer,
                            ign_limit integer,
                            k_count integer,
                            k_count_1 integer,
                            k_count_2 integer,
                            k_count_3 integer,
                            k_count_4 integer,
                            k_count_5 integer,
                            k_count_6 integer,
                            bat real,
                            cat_t real,
                            abs_lf real,
                            abs_rf real,
                            abs_lr real,
                            abs_rr real,
                            clutch_pos integer,
                            brake_press real,
                            steer_ang integer,
                            steer_trq integer,
                            g_lat real,
                            g_long real,
                            g_z integer,
                            yaw real,
                            eco integer,
                            fuel_used integer,
                            tc_v integer,
                            tc_ecuslip integer,
                            tc_r integer,
                            tc_lf integer,
                            tc_rf integer,
                            tc_lr integer,
                            tc_rr integer,
                            tc_slip integer,
                            tc_turn integer,
                            tc_overslip integer,
                            tc_out integer
                            )');
