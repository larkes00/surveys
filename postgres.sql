--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.4 (Ubuntu 12.4-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: surveys; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA surveys;


ALTER SCHEMA surveys OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: surveys_answer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.surveys_answer (
    id integer NOT NULL,
    content text NOT NULL
);


ALTER TABLE public.surveys_answer OWNER TO postgres;

--
-- Name: surveys_completesurvey; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.surveys_completesurvey (
    id integer NOT NULL,
    survey_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.surveys_completesurvey OWNER TO postgres;

--
-- Name: surveys_completesurvey_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.surveys_completesurvey_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.surveys_completesurvey_id_seq OWNER TO postgres;

--
-- Name: surveys_completesurvey_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.surveys_completesurvey_id_seq OWNED BY public.surveys_completesurvey.id;


--
-- Name: surveys_question; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.surveys_question (
    id integer NOT NULL,
    content text NOT NULL
);


ALTER TABLE public.surveys_question OWNER TO postgres;

--
-- Name: surveys_questionanswer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.surveys_questionanswer (
    id integer NOT NULL,
    answer_id integer NOT NULL
);


ALTER TABLE public.surveys_questionanswer OWNER TO postgres;

--
-- Name: surveys_questionanswer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.surveys_questionanswer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.surveys_questionanswer_id_seq OWNER TO postgres;

--
-- Name: surveys_questionanswer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.surveys_questionanswer_id_seq OWNED BY public.surveys_questionanswer.id;


--
-- Name: surveys_survey; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.surveys_survey (
    id integer NOT NULL,
    area_id integer NOT NULL
);


ALTER TABLE public.surveys_survey OWNER TO postgres;

--
-- Name: surveys_surveyarea; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.surveys_surveyarea (
    id integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.surveys_surveyarea OWNER TO postgres;

--
-- Name: surveys_surveyquestion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.surveys_surveyquestion (
    id integer NOT NULL,
    question_id integer NOT NULL,
    survey_id integer NOT NULL
);


ALTER TABLE public.surveys_surveyquestion OWNER TO postgres;

--
-- Name: surveys_surveyquestion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.surveys_surveyquestion_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.surveys_surveyquestion_id_seq OWNER TO postgres;

--
-- Name: surveys_surveyquestion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.surveys_surveyquestion_id_seq OWNED BY public.surveys_surveyquestion.id;


--
-- Name: surveys_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.surveys_user (
    id integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.surveys_user OWNER TO postgres;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: surveys_completesurvey id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_completesurvey ALTER COLUMN id SET DEFAULT nextval('public.surveys_completesurvey_id_seq'::regclass);


--
-- Name: surveys_questionanswer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_questionanswer ALTER COLUMN id SET DEFAULT nextval('public.surveys_questionanswer_id_seq'::regclass);


--
-- Name: surveys_surveyquestion id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_surveyquestion ALTER COLUMN id SET DEFAULT nextval('public.surveys_surveyquestion_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add answer	7	add_answer
26	Can change answer	7	change_answer
27	Can delete answer	7	delete_answer
28	Can view answer	7	view_answer
29	Can add question	8	add_question
30	Can change question	8	change_question
31	Can delete question	8	delete_question
32	Can view question	8	view_question
33	Can add survey area	9	add_surveyarea
34	Can change survey area	9	change_surveyarea
35	Can delete survey area	9	delete_surveyarea
36	Can view survey area	9	view_surveyarea
37	Can add user	10	add_user
38	Can change user	10	change_user
39	Can delete user	10	delete_user
40	Can view user	10	view_user
41	Can add survey	11	add_survey
42	Can change survey	11	change_survey
43	Can delete survey	11	delete_survey
44	Can view survey	11	view_survey
45	Can add complete survey	12	add_completesurvey
46	Can change complete survey	12	change_completesurvey
47	Can delete complete survey	12	delete_completesurvey
48	Can view complete survey	12	view_completesurvey
49	Can add survey question	13	add_surveyquestion
50	Can change survey question	13	change_surveyquestion
51	Can delete survey question	13	delete_surveyquestion
52	Can view survey question	13	view_surveyquestion
53	Can add question answer	14	add_questionanswer
54	Can change question answer	14	change_questionanswer
55	Can delete question answer	14	delete_questionanswer
56	Can view question answer	14	view_questionanswer
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$216000$klygmcG5VjcB$TcmuOTBOqd7L8sNmLu7lyOOE1amkx0NXoyG3PBjxN00=	2020-11-09 17:28:38.394564+02	t	admin			example@gmail.com	t	t	2020-11-09 17:28:25.906905+02
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2020-11-09 17:29:20.469557+02	1	User object (1)	1	[{"added": {}}]	10	1
2	2020-11-09 17:29:28.481121+02	2	User object (2)	1	[{"added": {}}]	10	1
3	2020-11-09 17:29:35.084175+02	3	User object (3)	1	[{"added": {}}]	10	1
4	2020-11-09 17:29:39.342442+02	4	User object (4)	1	[{"added": {}}]	10	1
5	2020-11-09 17:29:44.500381+02	5	User object (5)	1	[{"added": {}}]	10	1
6	2020-11-09 17:30:23.430619+02	1	SurveyArea object (1)	1	[{"added": {}}]	9	1
7	2020-11-09 17:30:28.50793+02	2	SurveyArea object (2)	1	[{"added": {}}]	9	1
8	2020-11-09 17:30:33.836027+02	3	SurveyArea object (3)	1	[{"added": {}}]	9	1
9	2020-11-09 17:30:39.0952+02	4	SurveyArea object (4)	1	[{"added": {}}]	9	1
10	2020-11-09 17:31:37.775874+02	1	Question object (1)	1	[{"added": {}}]	8	1
11	2020-11-09 17:31:51.849097+02	2	Question object (2)	1	[{"added": {}}]	8	1
12	2020-11-09 17:32:01.672241+02	3	Question object (3)	1	[{"added": {}}]	8	1
13	2020-11-09 17:32:10.213088+02	4	Question object (4)	1	[{"added": {}}]	8	1
14	2020-11-09 17:35:53.433018+02	1	Answer object (1)	1	[{"added": {}}]	7	1
15	2020-11-09 17:35:57.52857+02	2	Answer object (2)	1	[{"added": {}}]	7	1
16	2020-11-09 17:36:02.516297+02	3	Answer object (3)	1	[{"added": {}}]	7	1
17	2020-11-09 17:36:06.267971+02	4	Answer object (4)	1	[{"added": {}}]	7	1
18	2020-11-09 17:36:12.31635+02	5	Answer object (5)	1	[{"added": {}}]	7	1
19	2020-11-09 17:36:23.158024+02	6	Answer object (6)	1	[{"added": {}}]	7	1
20	2020-11-09 17:36:26.132098+02	7	Answer object (7)	1	[{"added": {}}]	7	1
21	2020-11-09 17:36:28.861891+02	8	Answer object (8)	1	[{"added": {}}]	7	1
22	2020-11-09 17:36:36.476872+02	9	Answer object (9)	1	[{"added": {}}]	7	1
23	2020-11-09 17:36:54.132806+02	10	Answer object (10)	1	[{"added": {}}]	7	1
24	2020-11-09 17:36:59.78395+02	11	Answer object (11)	1	[{"added": {}}]	7	1
25	2020-11-09 17:37:03.310255+02	12	Answer object (12)	1	[{"added": {}}]	7	1
26	2020-11-09 17:37:07.5325+02	13	Answer object (13)	1	[{"added": {}}]	7	1
27	2020-11-09 17:37:12.179342+02	14	Answer object (14)	1	[{"added": {}}]	7	1
28	2020-11-09 17:41:44.211932+02	1	Survey object (1)	1	[{"added": {}}]	11	1
29	2020-11-09 17:42:01.037607+02	2	Survey object (2)	1	[{"added": {}}]	11	1
30	2020-11-09 17:42:16.969553+02	2	Survey object (2)	3		11	1
31	2020-11-09 17:42:20.705189+02	1	Survey object (1)	3		11	1
32	2020-11-09 17:42:39.834017+02	1	Survey object (1)	1	[{"added": {}}]	11	1
33	2020-11-09 17:42:51.922769+02	2	Survey object (2)	1	[{"added": {}}]	11	1
34	2020-11-09 17:43:03.818748+02	3	Survey object (3)	1	[{"added": {}}]	11	1
35	2020-11-09 17:43:21.834454+02	4	Survey object (4)	1	[{"added": {}}]	11	1
36	2020-11-09 17:44:01.760438+02	5	Survey object (5)	1	[{"added": {}}]	11	1
37	2020-11-09 17:44:21.482885+02	6	Survey object (6)	1	[{"added": {}}]	11	1
38	2020-11-09 17:44:27.309446+02	7	Survey object (7)	1	[{"added": {}}]	11	1
39	2020-11-09 17:44:42.947894+02	8	Survey object (8)	1	[{"added": {}}]	11	1
40	2020-11-09 17:44:52.403607+02	9	Survey object (9)	1	[{"added": {}}]	11	1
41	2020-11-09 17:45:01.40937+02	10	Survey object (10)	1	[{"added": {}}]	11	1
42	2020-11-09 17:45:08.25637+02	11	Survey object (11)	1	[{"added": {}}]	11	1
43	2020-11-09 17:45:14.782348+02	12	Survey object (12)	1	[{"added": {}}]	11	1
44	2020-11-09 17:46:22.627449+02	12	Survey object (12)	3		11	1
45	2020-11-09 17:46:25.978557+02	11	Survey object (11)	3		11	1
46	2020-11-09 17:46:28.308536+02	10	Survey object (10)	3		11	1
47	2020-11-09 17:46:30.949388+02	9	Survey object (9)	3		11	1
48	2020-11-09 17:46:33.566762+02	8	Survey object (8)	3		11	1
49	2020-11-09 17:46:36.48423+02	7	Survey object (7)	3		11	1
50	2020-11-09 17:46:39.376218+02	6	Survey object (6)	3		11	1
51	2020-11-09 17:47:05.043518+02	6	Survey object (6)	1	[{"added": {}}]	11	1
52	2020-11-09 17:47:14.993569+02	7	Survey object (7)	1	[{"added": {}}]	11	1
53	2020-11-09 17:47:34.299062+02	8	Survey object (8)	1	[{"added": {}}]	11	1
54	2020-11-09 17:47:42.232072+02	9	Survey object (9)	1	[{"added": {}}]	11	1
55	2020-11-09 17:47:53.797951+02	10	Survey object (10)	1	[{"added": {}}]	11	1
56	2020-11-09 17:48:00.076045+02	11	Survey object (11)	1	[{"added": {}}]	11	1
57	2020-11-09 17:48:19.780508+02	12	Survey object (12)	1	[{"added": {}}]	11	1
58	2020-11-09 17:48:41.952201+02	13	Survey object (13)	1	[{"added": {}}]	11	1
59	2020-11-09 17:48:56.872171+02	1	CompleteSurvey object (1)	1	[{"added": {}}]	12	1
60	2020-11-09 17:49:00.964178+02	2	CompleteSurvey object (2)	1	[{"added": {}}]	12	1
61	2020-11-09 17:49:05.128458+02	3	CompleteSurvey object (3)	1	[{"added": {}}]	12	1
62	2020-11-09 17:49:11.210472+02	4	CompleteSurvey object (4)	1	[{"added": {}}]	12	1
63	2020-11-09 17:49:14.897374+02	5	CompleteSurvey object (5)	1	[{"added": {}}]	12	1
64	2020-11-09 17:49:19.437676+02	6	CompleteSurvey object (6)	1	[{"added": {}}]	12	1
65	2020-11-09 17:49:24.943914+02	7	CompleteSurvey object (7)	1	[{"added": {}}]	12	1
66	2020-11-09 17:49:30.924888+02	8	CompleteSurvey object (8)	1	[{"added": {}}]	12	1
67	2020-11-09 17:49:36.02957+02	9	CompleteSurvey object (9)	1	[{"added": {}}]	12	1
68	2020-11-09 17:49:42.91886+02	10	CompleteSurvey object (10)	1	[{"added": {}}]	12	1
69	2020-11-09 17:49:50.063893+02	11	CompleteSurvey object (11)	1	[{"added": {}}]	12	1
70	2020-11-09 17:49:53.034195+02	12	CompleteSurvey object (12)	1	[{"added": {}}]	12	1
71	2020-11-09 17:54:08.083955+02	13	Survey object (13)	2	[{"changed": {"fields": ["Answer"]}}]	11	1
72	2020-11-09 17:59:18.567586+02	9	Answer object (9)	3		7	1
73	2020-11-09 17:59:25.249117+02	9	Answer object (9)	2	[{"changed": {"fields": ["Id"]}}]	7	1
74	2020-11-09 17:59:51.216529+02	10	Answer object (10)	3		7	1
75	2020-11-09 17:59:59.138526+02	10	Answer object (10)	2	[{"changed": {"fields": ["Id"]}}]	7	1
76	2020-11-09 18:00:03.639856+02	11	Answer object (11)	3		7	1
77	2020-11-09 18:00:08.185748+02	11	Answer object (11)	2	[{"changed": {"fields": ["Id"]}}]	7	1
78	2020-11-09 18:00:11.635471+02	12	Answer object (12)	3		7	1
79	2020-11-09 18:00:16.154858+02	12	Answer object (12)	2	[{"changed": {"fields": ["Id"]}}]	7	1
80	2020-11-09 18:00:19.304666+02	13	Answer object (13)	3		7	1
81	2020-11-09 18:00:23.138389+02	13	Answer object (13)	2	[{"changed": {"fields": ["Id"]}}]	7	1
82	2020-11-09 18:00:27.485324+02	14	Answer object (14)	3		7	1
83	2020-11-09 18:00:27.510059+02	14	Answer object (14)	3		7	1
84	2020-11-09 18:01:55.156125+02	9	Survey object (9)	1	[{"added": {}}]	11	1
85	2020-11-09 18:02:05.498883+02	10	Survey object (10)	1	[{"added": {}}]	11	1
86	2020-11-09 18:02:15.578909+02	11	Survey object (11)	1	[{"added": {}}]	11	1
87	2020-11-09 18:02:22.315241+02	12	Survey object (12)	1	[{"added": {}}]	11	1
88	2020-11-09 18:02:33.48818+02	13	Survey object (13)	1	[{"added": {}}]	11	1
89	2020-11-09 18:02:56.186226+02	8	CompleteSurvey object (8)	3		12	1
90	2020-11-09 18:02:58.636267+02	7	CompleteSurvey object (7)	3		12	1
91	2020-11-09 18:03:01.297383+02	6	CompleteSurvey object (6)	3		12	1
92	2020-11-09 18:03:03.807989+02	5	CompleteSurvey object (5)	3		12	1
93	2020-11-09 18:03:05.922933+02	4	CompleteSurvey object (4)	3		12	1
94	2020-11-09 18:03:08.301052+02	3	CompleteSurvey object (3)	3		12	1
95	2020-11-09 18:03:10.72055+02	2	CompleteSurvey object (2)	3		12	1
96	2020-11-09 18:03:12.895787+02	1	CompleteSurvey object (1)	3		12	1
97	2020-11-09 18:03:17.367113+02	13	CompleteSurvey object (13)	1	[{"added": {}}]	12	1
98	2020-11-09 18:03:20.038307+02	14	CompleteSurvey object (14)	1	[{"added": {}}]	12	1
99	2020-11-09 18:03:22.763392+02	15	CompleteSurvey object (15)	1	[{"added": {}}]	12	1
100	2020-11-09 18:03:25.27589+02	16	CompleteSurvey object (16)	1	[{"added": {}}]	12	1
101	2020-11-09 18:03:28.255893+02	17	CompleteSurvey object (17)	1	[{"added": {}}]	12	1
102	2020-11-09 18:03:32.855797+02	18	CompleteSurvey object (18)	1	[{"added": {}}]	12	1
103	2020-11-09 18:03:36.006404+02	19	CompleteSurvey object (19)	1	[{"added": {}}]	12	1
104	2020-11-09 18:03:55.06506+02	20	CompleteSurvey object (20)	1	[{"added": {}}]	12	1
105	2020-11-09 18:04:01.525496+02	21	CompleteSurvey object (21)	1	[{"added": {}}]	12	1
106	2020-11-09 18:04:07.934931+02	22	CompleteSurvey object (22)	1	[{"added": {}}]	12	1
107	2020-11-09 18:04:13.473953+02	23	CompleteSurvey object (23)	1	[{"added": {}}]	12	1
108	2020-11-09 18:04:13.489237+02	24	CompleteSurvey object (24)	1	[{"added": {}}]	12	1
109	2020-11-09 18:04:20.146009+02	25	CompleteSurvey object (25)	1	[{"added": {}}]	12	1
110	2020-11-09 18:05:30.094934+02	14	CompleteSurvey object (14)	2	[{"changed": {"fields": ["User"]}}]	12	1
111	2020-11-09 18:05:35.882695+02	15	CompleteSurvey object (15)	2	[{"changed": {"fields": ["User"]}}]	12	1
112	2020-11-09 18:05:40.456705+02	16	CompleteSurvey object (16)	2	[{"changed": {"fields": ["User"]}}]	12	1
113	2020-11-09 18:05:46.764407+02	17	CompleteSurvey object (17)	2	[{"changed": {"fields": ["User"]}}]	12	1
114	2020-11-09 18:05:49.973813+02	17	CompleteSurvey object (17)	2	[]	12	1
115	2020-11-09 18:05:55.015899+02	18	CompleteSurvey object (18)	2	[]	12	1
116	2020-11-09 18:05:57.983765+02	19	CompleteSurvey object (19)	2	[]	12	1
117	2020-11-09 18:06:01.833132+02	20	CompleteSurvey object (20)	2	[]	12	1
118	2020-11-09 18:06:07.183435+02	21	CompleteSurvey object (21)	2	[]	12	1
119	2020-11-09 18:06:09.985259+02	22	CompleteSurvey object (22)	2	[]	12	1
120	2020-11-09 18:06:19.246215+02	23	CompleteSurvey object (23)	2	[{"changed": {"fields": ["User"]}}]	12	1
121	2020-11-09 18:06:28.671388+02	24	CompleteSurvey object (24)	2	[{"changed": {"fields": ["User", "Survey"]}}]	12	1
122	2020-11-09 18:06:54.225816+02	25	CompleteSurvey object (25)	3		12	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	surveys	answer
8	surveys	question
9	surveys	surveyarea
10	surveys	user
11	surveys	survey
12	surveys	completesurvey
13	surveys	surveyquestion
14	surveys	questionanswer
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-11-09 17:24:43.977936+02
2	auth	0001_initial	2020-11-09 17:24:44.359094+02
3	admin	0001_initial	2020-11-09 17:24:45.106835+02
4	admin	0002_logentry_remove_auto_add	2020-11-09 17:24:45.269281+02
5	admin	0003_logentry_add_action_flag_choices	2020-11-09 17:24:45.294458+02
6	contenttypes	0002_remove_content_type_name	2020-11-09 17:24:45.327287+02
7	auth	0002_alter_permission_name_max_length	2020-11-09 17:24:45.346461+02
8	auth	0003_alter_user_email_max_length	2020-11-09 17:24:45.379733+02
9	auth	0004_alter_user_username_opts	2020-11-09 17:24:45.404931+02
10	auth	0005_alter_user_last_login_null	2020-11-09 17:24:45.431422+02
11	auth	0006_require_contenttypes_0002	2020-11-09 17:24:45.450976+02
12	auth	0007_alter_validators_add_error_messages	2020-11-09 17:24:45.475667+02
13	auth	0008_alter_user_username_max_length	2020-11-09 17:24:45.589081+02
14	auth	0009_alter_user_last_name_max_length	2020-11-09 17:24:45.651286+02
15	auth	0010_alter_group_name_max_length	2020-11-09 17:24:45.703166+02
16	auth	0011_update_proxy_permissions	2020-11-09 17:24:45.728149+02
17	auth	0012_alter_user_first_name_max_length	2020-11-09 17:24:45.75618+02
18	sessions	0001_initial	2020-11-09 17:24:45.868545+02
19	surveys	0001_initial	2020-11-09 17:24:46.975856+02
22	surveys	0002_surveyquestion	2020-11-09 20:01:40.612921+02
23	surveys	0003_auto_20201111_1924	2020-11-11 21:24:53.24006+02
24	surveys	0003_questionanswer	2020-11-11 22:50:36.681859+02
25	surveys	0004_remove_survey_answer	2020-11-11 22:58:57.929441+02
26	surveys	0005_remove_survey_question	2020-11-12 09:17:49.786662+02
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
g3n59mfpxeppy9b1ojujavo8851zlmd0	.eJxVjMsOwiAQRf-FtSE8Cjgu3fsNZGYAqRqalHZl_HfbpAvdnnPufYuI61Lj2vMcxyQuQovTLyPkZ267SA9s90ny1JZ5JLkn8rBd3qaUX9ej_Tuo2Ou2zsCmBAWmpABmYCyBQLnMFgonW4xHvbGkPA3BO-3AeGv9mQjJZcvi8wX2Hzg_:1kc95y:rG_Hv0lbLZoWb4W2sRq69cnkjwS9Twc5jLQ8JvGgoVQ	2020-11-23 17:28:38.411797+02
\.


--
-- Data for Name: surveys_answer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.surveys_answer (id, content) FROM stdin;
1	30
2	33
3	21
4	23
5	40
6	Yes
7	Yes
8	Yes
9	7
10	8
11	5
12	10
13	Yes
14	No
15	1
16	2
17	Male
18	Female
19	No
20	YES
21	No
22	YES
23	No
24	YES
25	Ostrich
26	Cheetah
\.


--
-- Data for Name: surveys_completesurvey; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.surveys_completesurvey (id, survey_id, user_id) FROM stdin;
13	1	1
14	2	2
15	3	3
16	4	4
17	5	5
18	6	1
19	7	2
20	8	3
21	9	3
22	11	4
23	12	1
24	13	1
\.


--
-- Data for Name: surveys_question; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.surveys_question (id, content) FROM stdin;
1	How old are you?
2	Did you graduate from high school?
3	How do you rate medicine in your country from 1 to 10?
4	Should people protect nature?
5	What's your gender?
6	Are you from Ukraine?
7	Do you have a university degree
8	Did you get a job after graduating from university?
9	Need a change in healthcare?
10	In your opinion, it is necessary to stop deforestation?
11	Who do you think is faster than an ostrich or a cheetah?
\.


--
-- Data for Name: surveys_questionanswer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.surveys_questionanswer (id, answer_id) FROM stdin;
1	1
2	2
3	3
4	4
5	5
6	6
7	8
8	8
9	9
10	10
11	11
12	12
13	13
\.


--
-- Data for Name: surveys_survey; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.surveys_survey (id, area_id) FROM stdin;
1	1
2	1
3	1
4	1
5	1
6	2
7	2
8	2
9	3
10	3
11	3
12	3
13	4
\.


--
-- Data for Name: surveys_surveyarea; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.surveys_surveyarea (id, name) FROM stdin;
1	Personal
2	Education
3	Medicin
4	Nature
\.


--
-- Data for Name: surveys_surveyquestion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.surveys_surveyquestion (id, question_id, survey_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	1	5
6	2	6
7	2	7
8	2	8
9	3	9
10	3	10
11	3	11
12	3	12
13	4	13
\.


--
-- Data for Name: surveys_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.surveys_user (id, name) FROM stdin;
1	Tom
2	Ban
3	Bob
4	Alex
5	Steve
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 56, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 122, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 14, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- Name: surveys_completesurvey_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.surveys_completesurvey_id_seq', 25, true);


--
-- Name: surveys_questionanswer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.surveys_questionanswer_id_seq', 13, true);


--
-- Name: surveys_surveyquestion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.surveys_surveyquestion_id_seq', 13, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: surveys_answer surveys_answer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_answer
    ADD CONSTRAINT surveys_answer_pkey PRIMARY KEY (id);


--
-- Name: surveys_completesurvey surveys_completesurvey_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_completesurvey
    ADD CONSTRAINT surveys_completesurvey_pkey PRIMARY KEY (id);


--
-- Name: surveys_question surveys_question_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_question
    ADD CONSTRAINT surveys_question_pkey PRIMARY KEY (id);


--
-- Name: surveys_questionanswer surveys_questionanswer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_questionanswer
    ADD CONSTRAINT surveys_questionanswer_pkey PRIMARY KEY (id);


--
-- Name: surveys_survey surveys_survey_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_survey
    ADD CONSTRAINT surveys_survey_pkey PRIMARY KEY (id);


--
-- Name: surveys_surveyarea surveys_surveyarea_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_surveyarea
    ADD CONSTRAINT surveys_surveyarea_pkey PRIMARY KEY (id);


--
-- Name: surveys_surveyquestion surveys_surveyquestion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_surveyquestion
    ADD CONSTRAINT surveys_surveyquestion_pkey PRIMARY KEY (id);


--
-- Name: surveys_user surveys_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_user
    ADD CONSTRAINT surveys_user_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: surveys_completesurvey_survey_id_225a3e79; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX surveys_completesurvey_survey_id_225a3e79 ON public.surveys_completesurvey USING btree (survey_id);


--
-- Name: surveys_completesurvey_user_id_dfa57410; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX surveys_completesurvey_user_id_dfa57410 ON public.surveys_completesurvey USING btree (user_id);


--
-- Name: surveys_questionanswer_answer_id_ba44e856; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX surveys_questionanswer_answer_id_ba44e856 ON public.surveys_questionanswer USING btree (answer_id);


--
-- Name: surveys_survey_area_id_009448b5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX surveys_survey_area_id_009448b5 ON public.surveys_survey USING btree (area_id);


--
-- Name: surveys_surveyquestion_question_id_b34a84d5; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX surveys_surveyquestion_question_id_b34a84d5 ON public.surveys_surveyquestion USING btree (question_id);


--
-- Name: surveys_surveyquestion_survey_id_ca0121e7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX surveys_surveyquestion_survey_id_ca0121e7 ON public.surveys_surveyquestion USING btree (survey_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: surveys_completesurvey surveys_completesurvey_survey_id_225a3e79_fk_surveys_survey_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_completesurvey
    ADD CONSTRAINT surveys_completesurvey_survey_id_225a3e79_fk_surveys_survey_id FOREIGN KEY (survey_id) REFERENCES public.surveys_survey(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: surveys_completesurvey surveys_completesurvey_user_id_dfa57410_fk_surveys_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_completesurvey
    ADD CONSTRAINT surveys_completesurvey_user_id_dfa57410_fk_surveys_user_id FOREIGN KEY (user_id) REFERENCES public.surveys_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: surveys_questionanswer surveys_questionanswer_answer_id_ba44e856_fk_surveys_answer_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_questionanswer
    ADD CONSTRAINT surveys_questionanswer_answer_id_ba44e856_fk_surveys_answer_id FOREIGN KEY (answer_id) REFERENCES public.surveys_answer(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: surveys_survey surveys_survey_area_id_009448b5_fk_surveys_surveyarea_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_survey
    ADD CONSTRAINT surveys_survey_area_id_009448b5_fk_surveys_surveyarea_id FOREIGN KEY (area_id) REFERENCES public.surveys_surveyarea(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: surveys_surveyquestion surveys_surveyquesti_question_id_b34a84d5_fk_surveys_q; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_surveyquestion
    ADD CONSTRAINT surveys_surveyquesti_question_id_b34a84d5_fk_surveys_q FOREIGN KEY (question_id) REFERENCES public.surveys_question(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: surveys_surveyquestion surveys_surveyquestion_survey_id_ca0121e7_fk_surveys_survey_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.surveys_surveyquestion
    ADD CONSTRAINT surveys_surveyquestion_survey_id_ca0121e7_fk_surveys_survey_id FOREIGN KEY (survey_id) REFERENCES public.surveys_survey(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

