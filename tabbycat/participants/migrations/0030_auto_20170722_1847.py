# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0029_auto_20170706_1853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adjudicator',
            options={'ordering': ['tournament', 'institution', 'name'], 'verbose_name': 'adjudicator', 'verbose_name_plural': 'adjudicators'},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ['name'], 'verbose_name': 'institution', 'verbose_name_plural': 'institutions'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'person', 'verbose_name_plural': 'persons'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'region', 'verbose_name_plural': 'regions'},
        ),
        migrations.AlterModelOptions(
            name='speaker',
            options={'verbose_name': 'speaker', 'verbose_name_plural': 'speakers'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['tournament', 'institution', 'short_reference'], 'verbose_name': 'team', 'verbose_name_plural': 'teams'},
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='adj_core',
            field=models.BooleanField(default=False, verbose_name='adjudication core'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='breaking',
            field=models.BooleanField(default=False, verbose_name='breaking'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='conflicts',
            field=models.ManyToManyField(related_name='adj_adj_conflicts', through='adjallocation.AdjudicatorConflict', to='participants.Team', verbose_name='team conflicts'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='independent',
            field=models.BooleanField(default=False, verbose_name='independent'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Institution', verbose_name='institution'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='institution_conflicts',
            field=models.ManyToManyField(related_name='adj_inst_conflicts', through='adjallocation.AdjudicatorInstitutionConflict', to='participants.Institution', verbose_name='institution conflicts'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='test_score',
            field=models.FloatField(default=0, verbose_name='test score'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='tournament',
            field=models.ForeignKey(blank=True, help_text='Adjudicators not assigned to any tournament can be shared between tournaments', null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='tournament'),
        ),
        migrations.AlterField(
            model_name='adjudicator',
            name='url_key',
            field=models.SlugField(blank=True, max_length=24, null=True, unique=True, verbose_name='URL key'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='abbreviation',
            field=models.CharField(default='', help_text='For extremely confined spaces, e.g., "Camb", "VicWgtn"', max_length=8, verbose_name='abbreviation'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='code',
            field=models.CharField(help_text='What the institution is typically called for short, e.g., "Cambridge", "Vic Wellington"', max_length=20, verbose_name='code'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(help_text='The institution\'s full name, e.g., "University of Cambridge", "Victoria University of Wellington"', max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='participants.Region', verbose_name='region'),
        ),
        migrations.AlterField(
            model_name='person',
            name='anonymous',
            field=models.BooleanField(default=False, help_text='Anonymous persons will have their name and team redacted on public tab releases', verbose_name='anonymous'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], help_text='Gender is displayed in the adjudicator allocation interface, and nowhere else', max_length=1, verbose_name='gender'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(db_index=True, max_length=40, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='notes'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=40, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='person',
            name='pronoun',
            field=models.CharField(blank=True, help_text='If printing ballots using Tabbycat, there is the option to pre-print pronouns', max_length=10, verbose_name='pronoun'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Team', verbose_name='team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='break_categories',
            field=models.ManyToManyField(blank=True, to='breakqual.BreakCategory', verbose_name='break categories'),
        ),
        migrations.AlterField(
            model_name='team',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='divisions.Division', verbose_name='division'),
        ),
        migrations.AlterField(
            model_name='team',
            name='emoji',
            field=models.CharField(blank=True, choices=[('☕', '☕'), ('⛑', '⛑'), ('⛰', '⛰'), ('⛪', '⛪'), ('⛵', '⛵'), ('⛔', '⛔'), ('⛅', '⛅'), ('⛈', '⛈'), ('⛱', '⛱'), ('⛄', '⛄'), ('⚽', '⚽'), ('⛸', ''), ('⛏', '⛏'), ('😁', '😁'), ('😂', '😂'), ('😄', '😄'), ('😅', ''), ('😆', '😆'), ('😉', '😉'), ('😊', '😊'), ('😎', '😎'), ('😍', '😍'), ('😘', '😘'), ('😇', '😇'), ('😐', '😐'), ('😏', '😏'), ('😣', ''), ('😥', '😥'), ('😫', ''), ('😜', '😜'), ('😓', ''), ('😔', ''), ('😖', '😖'), ('😷', '😷'), ('😲', '😲'), ('😞', '😞'), ('😭', '😭'), ('😰', '😰'), ('😱', '😱'), ('😳', '😳'), ('😵', '😵'), ('😡', '😡'), ('👿', '👿'), ('👩', '👩'), ('👴', '👴'), ('👵', '👵'), ('👶', '👶'), ('👮', '👮'), ('👷', '👷'), ('👸', '👸'), ('💂', '💂'), ('🎅', '🎅'), ('👼', '👼'), ('👰', '👰'), ('🙅', '🙅'), ('🙆', '🙆'), ('🙋', '🙋'), ('🙇', '🙇'), ('🙌', '🙌'), ('🙏', '🙏'), ('💃', '💃'), ('💑', '💑'), ('👪', '👪'), ('👫', '👫'), ('👬', '👬'), ('👭', '👭'), ('💪', '💪'), ('👆', '👆'), ('✊', '✊'), ('✋', '✋'), ('👊', '👊'), ('👌', '👌'), ('👍', '👍'), ('👎', '👎'), ('👐', '👐'), ('💅', '💅'), ('👂', '👂'), ('👃', '👃'), ('👅', '👅'), ('👄', '👄'), ('💘', '💘'), ('💔', '💔'), ('💖', '💖'), ('💌', '💌'), ('💧', '💧'), ('💤', ''), ('💣', '💣'), ('💥', '💥'), ('💦', '💦'), ('💨', '💨'), ('💫', ''), ('👓', '👓'), ('👔', '👔'), ('👙', '👙'), ('👜', '👜'), ('👟', '👟'), ('👠', '👠'), ('👒', '👒'), ('🎩', '🎩'), ('💄', '💄'), ('💍', '💍'), ('💎', '💎'), ('👻', '👻'), ('💀', '💀'), ('👽', '👽'), ('👾', '👾'), ('💩', '💩'), ('🐵', ''), ('🙈', ''), ('🙉', ''), ('🙊', ''), ('🐶', '🐶'), ('🐩', ''), ('🐯', '🐯'), ('🐴', '🐴'), ('🐮', '🐮'), ('🐷', '🐷'), ('🐑', '🐑'), ('🐭', '🐭'), ('🐹', '🐹'), ('🐰', '🐰'), ('🐻', '🐻'), ('🐨', '🐨'), ('🐼', '🐼'), ('🐔', '🐔'), ('🐥', ''), ('🐦', '🐦'), ('🐧', '🐧'), ('🐸', '🐸'), ('🐢', ''), ('🐍', '🐍'), ('🐲', '🐲'), ('🐳', '🐳'), ('🐬', ''), ('🐟', '🐟'), ('🐠', ''), ('🐙', '🐙'), ('🐚', '🐚'), ('🐌', ''), ('🐛', ''), ('🐝', '🐝'), ('💐', ''), ('🌸', '🌸'), ('🌹', '🌹'), ('🌻', '🌻'), ('🌷', '🌷'), ('🌱', ''), ('🌴', ''), ('🌵', '🌵'), ('🌿', ''), ('🍀', ''), ('🍁', '🍁'), ('🍇', '🍇'), ('🍉', '🍉'), ('🍊', '🍊'), ('🍋', '🍋'), ('🍌', '🍌'), ('🍍', '🍍'), ('🍎', '🍎'), ('🍑', '🍑'), ('🍒', '🍒'), ('🍓', '🍓'), ('🍅', '🍅'), ('🍆', '🍆'), ('🌽', '🌽'), ('🍄', '🍄'), ('🍞', '🍞'), ('🍔', '🍔'), ('🍟', ''), ('🍕', '🍕'), ('🍙', ''), ('🍨', '🍨'), ('🍩', '🍩'), ('🍪', '🍪'), ('🍰', '🍰'), ('🍭', '🍭'), ('🍼', '🍼'), ('🍷', '🍷'), ('🍸', '🍸'), ('🍹', '🍹'), ('🍺', '🍺'), ('🍴', '🍴'), ('🌋', '🌋'), ('🏠', '🏠'), ('🏢', '🏢'), ('🏥', ''), ('🏩', '🏩'), ('🏰', ''), ('🌊', '🌊'), ('🎡', ''), ('🎢', ''), ('🎨', '🎨'), ('🚃', '🚃'), ('🚄', '🚄'), ('🚝', '🚝'), ('🚍', '🚍'), ('🚔', '🚔'), ('🚘', '🚘'), ('🚲', '🚲'), ('🚨', '🚨'), ('🚣', '🚣'), ('🚁', '🚁'), ('🚀', '🚀'), ('🚦', '🚦'), ('🚧', '🚧'), ('🚫', '🚫'), ('🚷', '🚷'), ('🚻', '🚻'), ('🚽', '🚽'), ('🚿', '🚿'), ('🛀', '🛀'), ('⏳', '⏳'), ('🌑', '🌑'), ('🌕', '🌕'), ('🌗', '🌗'), ('🌞', '🌞'), ('🌈', '🌈'), ('🌂', '🌂'), ('🌟', '🌟'), ('🔥', '🔥'), ('🎃', '🎃'), ('🎄', '🎄'), ('🎈', '🎈'), ('🎉', '🎉'), ('🎓', '🎓'), ('🎯', '🎯'), ('🎀', '🎀'), ('🏀', '🏀'), ('🏈', '🏈'), ('🎾', '🎾'), ('🎱', '🎱'), ('🏊', ''), ('🎮', '🎮'), ('🎲', '🎲'), ('📣', '📣'), ('📯', ''), ('🔔', '🔔'), ('🎶', '🎶'), ('🎤', '🎤'), ('🎹', '🎹'), ('🎺', '🎺'), ('🎻', '🎻'), ('📻', '📻'), ('📱', '📱'), ('📞', '📞'), ('🔋', '🔋'), ('🔌', '🔌'), ('💾', '💾'), ('💿', '💿'), ('🎬', '🎬'), ('📷', '📷'), ('🔍', '🔍'), ('🔭', '🔭'), ('💡', '💡'), ('📕', '📕'), ('📰', '📰'), ('💰', '💰'), ('💸', '💸'), ('📦', ''), ('📫', '📫'), ('💼', '💼'), ('📅', '📅'), ('📎', ''), ('📏', '📏'), ('📐', '📐'), ('🔑', '🔑'), ('🔩', '🔩'), ('💊', ''), ('🔪', '🔪'), ('🔫', '🔫'), ('🚬', '🚬'), ('🏁', ''), ('🔮', '🔮'), ('❌', '❌'), ('❓', '❓'), ('🔞', '🔞'), ('🆒', '🆒'), ('🆗', '🆗'), ('🆘', '🆘'), ('😙', '😙'), ('😑', '😑'), ('😮', '😮'), ('😴', '😴'), ('😛', '😛'), ('😧', '😧'), ('😬', '😬'), ('🕵', '🕵'), ('🖕', '🖕'), ('🖖', '🖖'), ('👁', '👁'), ('🕶', '🕶'), ('🛍', '🛍'), ('🐿', '🐿'), ('🕊', '🕊'), ('🕷', '🕷'), ('🌶', '🌶'), ('🏕', ''), ('🏛', '🏛'), ('🛢', '🛢'), ('🛥', ''), ('🛩', ''), ('🛎', '🛎'), ('🕰', '🕰'), ('🌡', '🌡'), ('🌤', '🌤'), ('🌧', '🌧'), ('🌩', '🌩'), ('🌪', '🌪'), ('🌬', '🌬'), ('🎖', '🎖'), ('🎗', '🎗'), ('🎞', '🎞'), ('🏋', ''), ('🏅', '🏅'), ('🕹', '🕹'), ('🎙', '🎙'), ('🖥', '🖥'), ('🖨', '🖨'), ('🖲', '🖲'), ('📸', ''), ('🕯', '🕯'), ('🗞', ''), ('🖋', '🖋'), ('🗑', '🗑'), ('🛠', ''), ('🗡', '🗡'), ('🛡', '🛡'), ('🏳', '🏳'), ('🏴', '🏴'), ('🤗', '🤗'), ('🤔', '🤔'), ('🙄', '🙄'), ('🤐', '🤐'), ('🤓', '🤓'), ('🙃', '🙃'), ('🤒', '🤒'), ('🤕', '🤕'), ('🤑', '🤑'), ('🤘', '🤘'), ('📿', '📿'), ('🤖', '🤖'), ('🦁', '🦁'), ('🦄', '🦄'), ('🦀', '🦀'), ('🦂', ''), ('🧀', '🧀'), ('🌭', '🌭'), ('🌮', '🌮'), ('🍿', '🍿'), ('🍾', '🍾'), ('🏏', '🏏'), ('🏐', '🏐'), ('🏓', '🏓'), ('🏹', '🏹'), ('🤣', '🤣'), ('🤤', '🤤'), ('🤢', '🤢'), ('🤧', '🤧'), ('🤠', '🤠'), ('🤡', '🤡'), ('🤥', '🤥'), ('🤴', '🤴'), ('🤵', '🤵'), ('🤰', '🤰'), ('🤶', '🤶'), ('🤦', '🤦'), ('🤷', '🤷'), ('🕺', '🕺'), ('🤺', '🤺'), ('🤸', '🤸'), ('🤹', '🤹'), ('🤳', '🤳'), ('🤞', '🤞'), ('🤙', '🤙'), ('🤛', '🤛'), ('🤜', '🤜'), ('🤚', '🤚'), ('🤝', '🤝'), ('🖤', '🖤'), ('🦊', '🦊'), ('🦌', '🦌'), ('🦇', '🦇'), ('🦅', '🦅'), ('🦆', '🦆'), ('🦉', '🦉'), ('🦎', '🦎'), ('🦈', '🦈'), ('🦐', '🦐'), ('🦑', '🦑'), ('🦋', '🦋'), ('🥀', '🥀'), ('🥝', '🥝'), ('🥑', '🥑'), ('🥔', '🥔'), ('🥕', '🥕'), ('🥒', '🥒'), ('🥜', '🥜'), ('🥐', '🥐'), ('🥖', '🥖'), ('🥞', '🥞'), ('🥙', '🥙'), ('🥚', '🥚'), ('🥗', '🥗'), ('🥛', '🥛'), ('🥂', '🥂'), ('🥃', '🥃'), ('🥄', '🥄'), ('🛶', '🛶'), ('🥊', '🥊'), ('🥋', '🥋'), ('🥅', '🥅'), ('🥁', '🥁'), ('🛒', '🛒')], default=None, max_length=2, null=True, verbose_name='emoji'),
        ),
        migrations.AlterField(
            model_name='team',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participants.Institution', verbose_name='institution'),
        ),
        migrations.AlterField(
            model_name='team',
            name='long_name',
            field=models.CharField(editable=False, help_text='The full name of the team, including institution name. (This is autogenerated.)', max_length=200, verbose_name='long name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='reference',
            field=models.CharField(blank=True, help_text='Do not include institution name (see "uses institutional prefix" below)', max_length=150, verbose_name='full name/suffix'),
        ),
        migrations.AlterField(
            model_name='team',
            name='short_name',
            field=models.CharField(editable=False, help_text='The name shown in the draw, including institution name. (This is autogenerated.)', max_length=50, verbose_name='short name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='short_reference',
            field=models.CharField(blank=True, help_text='The name shown in the draw. Do not include institution name (see "uses institutional prefix" below)', max_length=35, verbose_name='short name/suffix'),
        ),
        migrations.AlterField(
            model_name='team',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Tournament', verbose_name='tournament'),
        ),
        migrations.AlterField(
            model_name='team',
            name='type',
            field=models.CharField(choices=[('N', 'none'), ('S', 'swing'), ('C', 'composite'), ('B', 'bye')], default='N', max_length=1, verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='team',
            name='url_key',
            field=models.SlugField(blank=True, max_length=24, null=True, unique=True, verbose_name='URL key'),
        ),
        migrations.AlterField(
            model_name='team',
            name='use_institution_prefix',
            field=models.BooleanField(default=False, help_text='If ticked, a team called "1" from Victoria will be shown as "Victoria 1"', verbose_name='Uses institutional prefix'),
        ),
    ]