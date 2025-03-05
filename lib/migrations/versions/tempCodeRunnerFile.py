op.create_table('students',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(length=55), nullable=True),
    sa.Column('grade', sa.INTEGER(), nullable=True),
    sa.Column('birthday', sa.DATETIME(), nullable=True),
    sa.Column('enrolled_date', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_students_name', 'students', ['name'], unique=False)
    op.drop_index(op.f('ix_scholars_name'), table_name='scholars')
    op.drop_table('scholars')