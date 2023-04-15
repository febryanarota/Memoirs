# MEMOIRS

## Daftar Tabel Basis Data
| Nama Tabel | Atribut | <i>Type</i> | <i>Constraint</i> | <i>KEY</i>
| :---: | --- | --- | --- | ---
| `passcode` | passcode | CHAR(6) | - | PRIMARY KEY
| `article` | title<br/>tanggal<br/>content<br/>image | VARCHAR(100)<br/>VARCHAR(100)<br/>VARCHAR(5000)<br/>VARCHAR(100) | -<br/>-<br/>NOT NULL<br/>- | PRIMARY KEY<br/>-<br/>-<br/>-
| `to_do_list` | to_do<br/>tanggal<br/>done | VARCHAR(105)<br/>VARCHAR(100)<br/>INT | -<br/>-<br/>DEFAULT 0 | PRIMARY KEY<br/>PRIMARY KEY<br/>-
| `catatan_harian` | tanggal<br/>jam_mulai<br/>jam_berakhir<br/>nama_kegiatan | VARCHAR(100)<br/>VARCHAR(100)<br/>VARCHAR(100)<br/>VARCHAR(40) | -<br/>-<br/>-<br/>- | PRIMARY KEY<br/>PRIMARY KEY<br/>PRIMARY KEY<br/>PRIMARY KEY
| `catatan_target` | target<br/>tanggal | VARCHAR(1000)<br/>VARCHAR(100) | -<br/>- | PRIMARY KEY<br/>PRIMARY KEY
| `catatan_syukur` | syukur<br/>tanggal | VARCHAR(1000)<br/>VARCHAR(100) | -<br/>- | -<br/>PRIMARY KEY